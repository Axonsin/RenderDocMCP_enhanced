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

    # ==================== Draw Call / Action Operations ====================

    def get_draw_calls(
        self,
        include_children=True,
        marker_filter=None,
        exclude_markers=None,
        event_id_min=None,
        event_id_max=None,
        only_actions=False,
        flags_filter=None,
    ):
        """Get all draw calls/actions in the capture with optional filtering"""
        return self._action.get_draw_calls(
            include_children=include_children,
            marker_filter=marker_filter,
            exclude_markers=exclude_markers,
            event_id_min=event_id_min,
            event_id_max=event_id_max,
            only_actions=only_actions,
            flags_filter=flags_filter,
        )

    def get_frame_summary(self):
        """Get a summary of the current capture frame"""
        return self._action.get_frame_summary()

    def get_draw_call_details(self, event_id):
        """Get detailed information about a specific draw call"""
        return self._action.get_draw_call_details(event_id)

    def get_action_timings(self, event_ids=None, marker_filter=None, exclude_markers=None):
        """Get GPU timing information for actions"""
        return self._action.get_action_timings(
            event_ids=event_ids,
            marker_filter=marker_filter,
            exclude_markers=exclude_markers,
        )

    def inspect_event(self, event_id):
        """Get a compact analysis-oriented event inspection bundle."""
        return self._analysis.inspect_event(event_id)

    def summarize_capture(self):
        """Get a high-level summary of the current capture."""
        return self._analysis.summarize_capture()

    # ==================== Search Operations ====================

    def search_draws(self, by, query, stage=None):
        """Search draw calls using a canonical search interface."""
        return self._search.search_draws(by, query, stage)

    # ==================== Resource Operations ====================

    def list_resources(self, resource_type, name_filter=None, offset=0, limit=50):
        """List resources using a canonical resource-listing interface."""
        return self._resource.list_resources(resource_type, name_filter, offset, limit)

    def get_buffer_contents(self, resource_id, offset=0, length=0):
        """Get buffer data"""
        return self._resource.get_buffer_contents(resource_id, offset, length)

    def get_texture_info(self, resource_id):
        """Get texture metadata"""
        return self._resource.get_texture_info(resource_id)

    def get_texture_data(self, resource_id, mip=0, slice=0, sample=0, depth_slice=None):
        """Get texture pixel data"""
        return self._resource.get_texture_data(resource_id, mip, slice, sample, depth_slice)

    def save_texture(
        self,
        resource_id,
        output_path,
        format_type="PNG",
        mip=0,
        slice_index=0,
        alpha_mode="preserve",
    ):
        """Save texture to file"""
        return self._resource.save_texture(
            resource_id=resource_id,
            output_path=output_path,
            format_type=format_type,
            mip=mip,
            slice_index=slice_index,
            alpha_mode=alpha_mode,
        )

    # ==================== Pipeline Operations ====================

    def get_shader_info(self, event_id, stage):
        """Get shader information for a specific stage"""
        return self._pipeline.get_shader_info(event_id, stage)

    def get_shader_source(self, event_id, stage):
        """Get original shader source text for a specific stage when available."""
        return self._pipeline.get_shader_source(event_id, stage)

    def get_pipeline_state(self, event_id):
        """Get full pipeline state at an event"""
        return self._pipeline.get_pipeline_state(event_id)

    def trace_resource_usage(
        self,
        resource_id,
        marker_filter=None,
        exclude_markers=None,
        event_id_min=None,
        event_id_max=None,
        before_event_id=None,
    ):
        """Trace how a resource is used across matching events."""
        return self._analysis.trace_resource_usage(
            resource_id=resource_id,
            marker_filter=marker_filter,
            exclude_markers=exclude_markers,
            event_id_min=event_id_min,
            event_id_max=event_id_max,
            before_event_id=before_event_id,
        )

    def trace_event_dependencies(self, event_id):
        """Trace the resource dependencies of an event."""
        return self._analysis.trace_event_dependencies(event_id)

    def diff_events(self, event_id_a, event_id_b):
        """Compare two events."""
        return self._analysis.diff_events(event_id_a, event_id_b)

    def analyze_pass(self, marker_filter, exclude_markers=None):
        """Summarize work under a marker subtree."""
        return self._analysis.analyze_pass(marker_filter, exclude_markers)

    # ==================== Mesh Operations ====================

    def get_mesh_summary(self, event_id):
        """Get mesh summary information for a draw call"""
        return self._mesh.get_mesh_summary(event_id)

    def get_mesh_data(
        self,
        event_id,
        stage="VSIn",
        offset=0,
        limit=100,
        start_offset=0,
        max_vertices=100,
        attributes=None,
    ):
        """Get mesh vertex and index data for a draw call (with pagination)"""
        return self._mesh.get_mesh_data(
            event_id=event_id,
            stage=stage,
            offset=offset,
            limit=limit,
            start_offset=start_offset,
            max_vertices=max_vertices,
            attributes=attributes,
        )

    def export_mesh_csv(
        self,
        event_id,
        output_path,
        stage="VSIn",
        include_attributes=None,
    ):
        """Export mesh data to CSV file"""
        return self._mesh.export_mesh_csv(event_id, output_path, stage, include_attributes)
