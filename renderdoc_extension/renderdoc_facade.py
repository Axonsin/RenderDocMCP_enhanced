"""
RenderDoc API Facade
Provides thread-safe access to RenderDoc's ReplayController and CaptureContext.
Uses BlockInvoke to marshal calls to the replay thread.
"""

from .services import (
    CaptureManager,
    ActionService,
    SearchService,
    ResourceService,
    PipelineService,
    ShaderEditService,
    MeshService,
    AnalysisService,
)


class RenderDocFacade:
    """
    Facade for RenderDoc API access.

    This class delegates all operations to specialized service classes:
    - CaptureManager: Capture management (status, list, open)
    - ActionService: Draw call / action operations
    - SearchService: Reverse lookup searches
    - ResourceService: Texture and buffer data
    - PipelineService: Pipeline state and shader info
    - MeshService: Mesh data operations
    """

    def __init__(self, ctx):
        """
        Initialize facade with CaptureContext.

        Args:
            ctx: The pyrenderdoc CaptureContext from register()
        """
        self.ctx = ctx

        # Initialize service classes
        self._capture = CaptureManager(ctx, self._invoke)
        self._action = ActionService(ctx, self._invoke)
        self._search = SearchService(ctx, self._invoke)
        self._resource = ResourceService(ctx, self._invoke)
        self._pipeline = PipelineService(ctx, self._invoke)
        self._shader_edit = ShaderEditService(ctx, self._invoke)
        self._mesh = MeshService(ctx, self._invoke)
        self._analysis = AnalysisService(
            ctx,
            self._invoke,
            self._action,
            self._pipeline,
            self._resource,
            self._mesh,
        )

    def _invoke(self, callback):
        """Invoke callback on replay thread via BlockInvoke"""
        self.ctx.Replay().BlockInvoke(callback)

    def dispose(self):
        """Revert owned shader edits before the extension unloads."""
        self._shader_edit.dispose()
        self._pipeline.dispose()

    # ==================== Capture Management ====================

    def get_capture_status(self):
        """Check if a capture is loaded and get API info"""
        return self._capture.get_capture_status()

    def list_captures(self, directory):
        """List all .rdc files in the specified directory"""
        return self._capture.list_captures(directory)

    def open_capture(self, capture_path):
        """Open a capture file in RenderDoc"""
        return self._capture.open_capture(capture_path)

    # ==================== Action Operations ====================

    def get_actions(
        self,
        include_children=True,
        marker_filter=None,
        exclude_markers=None,
        action_event_id_range=None,
        exclude_marker_actions=False,
        flags_filter=None,
    ):
        """Get the action tree in the capture with optional filtering"""
        return self._action.get_actions(
            include_children=include_children,
            marker_filter=marker_filter,
            exclude_markers=exclude_markers,
            action_event_id_range=action_event_id_range,
            exclude_marker_actions=exclude_marker_actions,
            flags_filter=flags_filter,
        )

    def get_frame_summary(self):
        """Get a summary of the current capture frame"""
        return self._action.get_frame_summary()

    def get_action_details(self, action_event_id):
        """Get metadata, draw counts, offsets and output resources for an action."""
        return self._action.get_action_details(action_event_id=action_event_id)

    def get_action_api_calls(self, action_event_id, api_event_id=None, child_path=None,
                             offset=0, limit=50):
        return self._action.get_action_api_calls(
            action_event_id, api_event_id, child_path, offset, limit)

    def get_action_timings(self, action_event_ids=None, marker_filter=None, exclude_markers=None):
        """Get GPU timing information for actions"""
        return self._action.get_action_timings(
            action_event_ids=action_event_ids,
            marker_filter=marker_filter,
            exclude_markers=exclude_markers,
        )

    def inspect_action(self, action_event_id):
        """Get a compact analysis-oriented action inspection bundle."""
        return self._analysis.inspect_action(action_event_id)

    def summarize_capture(self):
        """Get a high-level summary of the current capture."""
        return self._analysis.summarize_capture()

    # ==================== Search Operations ====================

    def search_actions(self, by, query, stage=None):
        """Search draw and dispatch actions by shader, texture or resource."""
        return self._search.search_actions(by, query, stage)

    # ==================== Resource Operations ====================

    def list_resources(self, resource_type="all", name_filter=None, offset=0, limit=50,
                       sort_by="name"):
        """List resources using a canonical resource-listing interface."""
        return self._resource.list_resources(resource_type, name_filter, offset, limit, sort_by)

    def inspect_resource(self, resource_id, related_offset=0, related_limit=50):
        return self._resource.inspect_resource(resource_id, related_offset, related_limit)

    def get_resource_initialization(self, resource_id, chunk_index=None,
                                    child_path=None, offset=0, limit=50):
        return self._resource.get_resource_initialization(
            resource_id, chunk_index, child_path, offset, limit)

    def get_buffer_contents(self, resource_id, offset=0, length=0):
        """Get buffer data"""
        return self._resource.get_buffer_contents(resource_id, offset, length)

    def get_texture_info(self, resource_id):
        """Get texture metadata"""
        return self._resource.get_texture_info(resource_id)

    def get_texture_data(self, resource_id, mip=0, slice_index=0, sample=0, depth_slice=None, action_event_id=None):
        """Get texture pixel data"""
        return self._resource.get_texture_data(resource_id, mip, slice_index, sample, depth_slice, action_event_id)

    def save_texture(
        self,
        resource_id,
        output_path,
        format_type="PNG",
        mip=0,
        slice_index=0,
        alpha_mode="preserve",
        action_event_id=None,
    ):
        """Save texture to file"""
        return self._resource.save_texture(
            resource_id=resource_id,
            output_path=output_path,
            format_type=format_type,
            mip=mip,
            slice_index=slice_index,
            alpha_mode=alpha_mode,
            action_event_id=action_event_id,
        )

    # ==================== Pipeline Operations ====================

    def get_shader_info(self, event_id, stage):
        """Get shader information for a specific stage"""
        return self._pipeline.get_shader_info(event_id, stage)

    def get_shader_source(self, event_id, stage):
        """Get original shader source text for a specific stage when available."""
        return self._pipeline.get_shader_source(event_id, stage)

    def get_shader_edit_context(self, event_id, stage, mode="auto"):
        return self._shader_edit.get_shader_edit_context(event_id, stage, mode)

    def replace_shader(self, edit_id, source_text):
        return self._shader_edit.replace_shader(edit_id, source_text)

    def revert_shader(self, edit_id):
        return self._shader_edit.revert_shader(edit_id)

    def list_shader_replacements(self):
        return self._shader_edit.list_shader_replacements()

    def export_shader_source(self, edit_id, output_path):
        return self._shader_edit.export_shader_source(edit_id, output_path)

    def get_pipeline_state(self, action_event_id):
        return self._pipeline.get_pipeline_state(action_event_id)

    def get_pipeline_stage(self, action_event_id, stage, section="overview",
                           show_unused=False, show_empty=False, offset=0, limit=50):
        return self._pipeline.get_pipeline_stage(action_event_id, stage, section,
                                                show_unused, show_empty, offset, limit)

    def inspect_pipeline_binding(self, action_event_id, binding_id, section="details",
                                 child_path=None, offset=0, limit=50):
        return self._pipeline.inspect_pipeline_binding(action_event_id, binding_id, section,
                                                      child_path, offset, limit)

    def get_action_textures(self, action_event_id, direction="all", stage=None,
                            show_unused=False, show_empty=False, offset=0, limit=50):
        return self._pipeline.get_action_textures(action_event_id, direction, stage,
                                                 show_unused, show_empty, offset, limit)

    def trace_resource_usage(
        self,
        resource_id,
        marker_filter=None,
        exclude_markers=None,
        event_id_range=None,
        before_event_id=None,
        offset=0,
        limit=100,
        categories=None,
    ):
        """Trace how a resource is used across matching events."""
        return self._analysis.trace_resource_usage(
            resource_id=resource_id,
            marker_filter=marker_filter,
            exclude_markers=exclude_markers,
            event_id_range=event_id_range,
            before_event_id=before_event_id,
            offset=offset,
            limit=limit,
            categories=categories,
        )

    def trace_action_dependencies(self, action_event_id):
        """Trace the resource dependencies of an action."""
        return self._analysis.trace_action_dependencies(action_event_id)

    def diff_actions(self, action_event_id_a, action_event_id_b):
        """Compare two actions."""
        return self._analysis.diff_actions(action_event_id_a, action_event_id_b)

    def analyze_pass(self, marker_filter, exclude_markers=None):
        """Summarize work under a marker subtree."""
        return self._analysis.analyze_pass(marker_filter, exclude_markers)

    # ==================== Mesh Operations ====================

    def get_mesh_summary(self, action_event_id):
        """Get mesh summary information for a draw call"""
        return self._mesh.get_mesh_summary(action_event_id)

    def get_mesh_data(
        self,
        action_event_id,
        stage="VSIn",
        offset=0,
        limit=100,
        attributes=None,
    ):
        """Get mesh vertex and index data for a draw call (with pagination)"""
        return self._mesh.get_mesh_data(
            action_event_id=action_event_id,
            stage=stage,
            offset=offset,
            limit=limit,
            attributes=attributes,
        )

    def export_mesh_csv(
        self,
        action_event_id,
        output_path,
        stage="VSIn",
        attributes=None,
    ):
        """Export mesh data to CSV file"""
        return self._mesh.export_mesh_csv(action_event_id, output_path, stage, attributes)
