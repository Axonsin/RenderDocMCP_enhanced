"""Exception-safe event-scoped replay reads (Python 3.6 compatible)."""


import sys
import time

def guard_for(ctx):
    module = sys.modules.get(__package__ + ".replay_guard")
    return module.GUARDS.get(id(ctx)) if module else None


def action_for(ctx, event_id):
    guard = guard_for(ctx)
    if guard and getattr(guard.thread_state, "active", False):
        return guard.actions.get(event_id)
    return ctx.GetAction(event_id)


def require_action(ctx, event_id):
    guard = guard_for(ctx)
    active = guard and getattr(guard.thread_state, "active", False)
    if not active and not ctx.IsCaptureLoaded():
        raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")
    if type(event_id) is not int or event_id <= 0:
        raise ValueError("INVALID_ACTION_EVENT_ID: positive integer required")
    action = action_for(ctx, event_id)
    if action is None or action.eventId != event_id:
        raise ValueError("INVALID_ACTION_EVENT_ID: exact action event required")
    return action


def at_event(ctx, invoke, event_id, operation, require_exact_action=True):
    """Never let a Python exception or replay-owned object escape a SWIG callback."""
    guard = guard_for(ctx)
    active = guard and getattr(guard.thread_state, "active", False)
    if not active and not ctx.IsCaptureLoaded():
        raise ValueError("CAPTURE_NOT_LOADED: no capture loaded")
    if event_id is not None and require_exact_action:
        require_action(ctx, event_id)
    restore = getattr(guard.thread_state, "event", guard.state.get("event_id")) if active else ctx.CurEvent()
    target = restore if event_id is None else event_id
    result = {}
    guard = guard_for(ctx)

    def callback(controller):
        try:
            if guard:
                guard.check(controller)
                guard.phase("replay", target_event_id=target, restore_event_id=restore)
            controller.SetFrameEvent(target, True)
            if guard:
                guard.thread_state.event = target
            if guard:
                guard.check(controller)
            result["value"] = operation(controller, target)
            if guard:
                guard.check(controller)
        except Exception as exc:
            result["error"] = (isinstance(exc, ValueError), str(exc))
        finally:
            try:
                if guard:
                    guard.phase("restoring_event")
                controller.SetFrameEvent(restore, True)
                if guard:
                    guard.thread_state.event = restore
                if guard:
                    guard.check(controller)
            except Exception as exc:
                previous = result.get("error", (False, ""))[1]
                result["error"] = (False, "REPLAY_RESTORE_FAILED: %s; previous error: %s" % (exc, previous))

    invoke(callback)
    if "error" in result:
        invalid, message = result["error"]
        raise (ValueError if invalid else RuntimeError)(message)
    return result.get("value")


def record_restore_failure(target, exc):
    """Store a REPLAY_RESTORE_FAILED error on a result dict, preserving any prior error.

    The stable prefix always leads so request classification stays correct even
    when a previous error (e.g. INVALID_MARKER_FILTER) is being merged in.
    """
    previous = target.get("error")
    if isinstance(previous, BaseException):
        previous_text = str(previous.args[0]) if previous.args else str(previous)
    else:
        previous_text = str(previous or "")
    if previous_text:
        target["error"] = RuntimeError(
            "REPLAY_RESTORE_FAILED: %s (previous error: %s)" % (exc, previous_text)
        )
    else:
        target["error"] = RuntimeError("REPLAY_RESTORE_FAILED: %s" % exc)
