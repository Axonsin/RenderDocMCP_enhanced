"""Explicit adapters for RenderDoc 1.46 replay structures, not SWIG introspection."""
import math

import renderdoc as rd


FIELDS = {
    "Viewport": "x y width height minDepth maxDepth enabled",
    "Scissor": "x y width height enabled",
    "BlendEquation": "source destination operation",
    "ColorBlend": "enabled logicOperationEnabled writeMask colorBlend alphaBlend logicOperation",
    "VertexInputAttribute": "name vertexBuffer byteOffset perInstance instanceRate format genericValue genericEnabled floatCastWrong used",
    "Descriptor": "type flags format resource secondary view byteOffset byteSize elementByteSize firstMip numMips firstSlice numSlices textureType swizzle minLODClamp counterByteOffset bufferStructCount",
    "SamplerDescriptor": "object type addressU addressV addressW borderColorValue borderColorType compareFunction filter mipBias minLOD maxLOD maxAnisotropy seamlessCubemaps unnormalized creationTimeConstant srgbBorder swizzle ycbcrSampler ycbcrModel ycbcrRange xChromaOffset yChromaOffset chromaFilter forceExplicitReconstruction",
    "RasterizerState": "fillMode cullMode frontCCW depthBias depthBiasClamp slopeScaledDepthBias depthClip scissorEnable multisampleEnable antialiasedLines rasterizerDiscard lineWidth depthClampEnable conservativeRasterization",
    "Rasterizer": "fillMode cullMode frontCCW depthBias depthBiasClamp slopeScaledDepthBias depthClip scissorEnable multisampleEnable antialiasedLines rasterizerDiscard lineWidth depthClampEnable conservativeRasterization viewports scissors",
    "DepthState": "depthEnable depthFunction depthWrites",
    "DepthStencil": "depthTestEnable depthWriteEnable depthFunction depthBoundsEnable minDepthBounds maxDepthBounds stencilTestEnable frontFace backFace",
    "StencilFace": "function failOperation depthFailOperation passOperation compareMask writeMask reference",
    "Multisample": "rasterSamples sampleShadingEnable minSampleShading sampleMask alphaToCoverageEnable alphaToOneEnable",
    "DynamicOffset": "descriptorByteOffset dynamicBufferByteOffset",
    "FloatVector": "x y z w",
    "PixelValue": "floatValue uintValue intValue",
    "TextureFilter": "minify magnify mip filter",
    "SamplerFilter": "minify magnify mip filter",
    "VKSampleLocations": "gridWidth gridHeight customLocations",
    "RasterState": "fillMode cullMode frontCCW",
    "DepthTestState": "depthFunction depthBounds minDepthBounds maxDepthBounds depthEnable depthWrites",
    "VKRasterizer": "depthBias slopeScaledDepthBias depthBiasClamp fillMode cullMode lineStippleFactor pipelineShadingRate lineStipplePattern provokingVertexFirst shadingRateCombiners frontCCW extraPrimitiveOverestimationSize depthBiasEnable depthBiasExact lineRasterMode depthClampEnable depthClipEnable rasterizerDiscardEnable lineWidth conservativeRasterization depthBiasRepresentation",
    "VKDepthStencil": "frontFace backFace depthFunction depthWriteEnable depthBoundsEnable minDepthBounds maxDepthBounds depthTestEnable stencilTestEnable",
    "VKMultisample": "minSampleShading rasterSamples sampleShadingEnable sampleMask sampleLocations",
    "D3D11RasterizerState": "depthBias slopeScaledDepthBias depthBiasClamp fillMode cullMode depthClip resourceId antialiasedLines frontCCW multisampleEnable forcedSampleCount scissorEnable conservativeRasterization",
    "D3D12RasterizerState": "depthBias slopeScaledDepthBias depthBiasClamp fillMode cullMode depthClip baseShadingRate shadingRateCombiners shadingRateImage frontCCW forcedSampleCount lineRasterMode conservativeRasterization",
    "GLRasterizerState": "depthBias slopeScaledDepthBias sampleShading sampleCoverageInvert programmablePointSize pointSize fillMode cullMode minSampleShadingRate offsetClamp sampleMaskValue alphaToOne frontCCW sampleCoverageValue pointOriginUpperLeft depthClamp multisampleEnable sampleMask sampleCoverage alphaToCoverage lineWidth pointFadeThreshold",
    "VKCurrentPass": "renderpass framebuffer renderArea colorFeedbackAllowed depthFeedbackAllowed stencilFeedbackAllowed",
    "RenderArea": "x y width height",
    "TextureSwizzle4": "red green blue alpha",
}
REQUIRED = {"Viewport": ("x", "y", "width", "height"),
            "Scissor": ("x", "y", "width", "height"),
            "ColorBlend": ("enabled", "colorBlend", "alphaBlend", "writeMask"),
            "BlendEquation": ("source", "destination", "operation"),
            "VertexInputAttribute": ("vertexBuffer", "byteOffset", "format"),
            "SamplerDescriptor": ("addressU", "addressV", "addressW", "filter"),
            "Descriptor": ("type", "resource", "byteOffset", "byteSize"),
            "RasterState": ("fillMode", "cullMode", "frontCCW"),
            "DepthTestState": ("depthEnable", "depthWrites", "depthFunction")}
# Explicit field vocabulary for API-specific native wrappers whose Python class
# names differ between generators. Unknown fields are never guessed via dir().
NATIVE_FIELDS = set(" ".join(FIELDS.values()).split()) | set("""
depthEnable depthFunction depthWrites stencilEnable stencilFunction failOp depthFailOp passOp
depthTestFunction stencilRef readMask renderPass framebuffer inputAttachments colorAttachments
resolveAttachments depthstencilAttachment depthstencilResolveAttachment images attachments
begin end resourceId imageResourceId viewResourceId imageLayout baseMip baseLayer numLayers
firstMip numMips firstSlice numSlices descriptorSetResourceId layoutResourceId pushDescriptor
dynamicOffsets descriptorBuffers offset size byteOffset byteSize descriptorByteOffset
dynamicBufferByteOffset imageLayouts layouts layout enabled sampleCount mask
depthBiasEnable depthClamp depthClipEnable conservativeRaster overestimationSize
primitiveOverestimationSize provokingVertexMode lineRasterMode lineStippleEnable
lineStippleFactor lineStipplePattern discardRectangleMode discardRectangles
fragmentShadingRate fragmentShadingRateCombinerOps sampleLocationsEnable sampleLocations
shadingRateImageEnable pipelineResourceId descriptorBufferResourceId addressModeU addressModeV
addressModeW mipLODBias mipFilter minFilter magFilter useBorderColor compareEnable compare
anisotropyEnable borderColorType unnormalizedCoordinates seamlessCubemaps maxAnisotropy
""".split())


def plain(value, depth=0):
    if value is None or isinstance(value, (str, bool)):
        return value
    if isinstance(value, rd.ResourceId):
        return "ResourceId::%d" % int(value)
    if hasattr(value, "name") and isinstance(value, int):
        return value.name
    if isinstance(value, (int, float)):
        return str(value) if isinstance(value, float) and not math.isfinite(value) else value
    if depth > 12:
        raise ValueError("SERIALIZATION_UNAVAILABLE: structure depth exceeded")
    if hasattr(value, "Name") and callable(value.Name):
        return value.Name()
    if isinstance(value, (bytes, bytearray)):
        return {"byte_size": len(value)}
    if isinstance(value, dict):
        return {str(k): plain(v, depth + 1) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [plain(v, depth + 1) for v in value]
    if hasattr(value, "__iter__") or (hasattr(value, "__len__") and hasattr(value, "__getitem__")):
        try:
            return [plain(v, depth + 1) for v in value]
        except TypeError:
            pass
    name = type(value).__name__
    schema = FIELDS.get(name)
    if schema:
        missing = [k for k in REQUIRED.get(name, ()) if not hasattr(value, k)]
        if missing:
            raise ValueError("SERIALIZATION_UNAVAILABLE: %s missing %s" % (name, missing))
        names = schema.split()
    elif name == "SimpleNamespace":
        # Test/adaptor objects explicitly expose their data; this is not used
        # as a discovery mechanism for native SWIG replay structs.
        names = list(vars(value))
    else:
        names = [k for k in sorted(NATIVE_FIELDS) if hasattr(value, k)]
    result = {}
    for key in names:
        if hasattr(value, key):
            member = getattr(value, key)
            if not callable(member):
                result[key] = plain(member, depth + 1)
    if not result:
        raise ValueError("SERIALIZATION_UNAVAILABLE: unsupported native type %s" % name)
    return result
