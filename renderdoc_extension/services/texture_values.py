"""Typed numeric texture decoding. No preview conversion or tone mapping."""
import math
import struct


MAX_SUBRESOURCE_BYTES = 64 * 1024 * 1024
MAX_ROI_PIXELS = 262144


def _ufloat(bits, mantissa):
    exponent = bits >> mantissa
    fraction = bits & ((1 << mantissa) - 1)
    if exponent == 31:
        return float("nan") if fraction else float("inf")
    if exponent == 0:
        return math.ldexp(float(fraction), -14 - mantissa)
    return math.ldexp(1.0 + fraction / float(1 << mantissa), exponent - 15)


def decoder(fmt):
    kind = str(fmt.type).split(".")[-1]
    comp = str(fmt.compType).split(".")[-1]
    # Real IntEnums expose .name; SWIG enum stringification also works.
    kind = getattr(fmt.type, "name", kind)
    comp = getattr(fmt.compType, "name", comp)
    srgb = comp == "UNormSRGB"
    if kind == "Regular":
        width, count = int(fmt.compByteWidth), int(fmt.compCount)
        if not 1 <= count <= 4:
            raise ValueError("UNSUPPORTED_FORMAT: invalid component count")
        if comp == "Float" and width in (2, 4, 8):
            code = {2: "e", 4: "f", 8: "d"}[width]
        elif comp in ("UInt", "SInt", "UNorm", "SNorm", "UNormSRGB") and width in (1, 2, 4):
            code = ({1: "b", 2: "h", 4: "i"} if comp in ("SInt", "SNorm") else
                    {1: "B", 2: "H", 4: "I"})[width]
        else:
            raise ValueError("UNSUPPORTED_FORMAT: %s width %s" % (comp, width))
        size = width * count
        def unpack(data, offset):
            values = list(struct.unpack_from("<%d%s" % (count, code), data, offset))
            if comp in ("UNorm", "UNormSRGB"):
                values = [v / float((1 << (width * 8)) - 1) for v in values]
            elif comp == "SNorm":
                values = [max(-1.0, v / float((1 << (width * 8 - 1)) - 1)) for v in values]
            return values
    elif kind in ("R10G10B10A2", "R11G11B10"):
        size, count = 4, 4 if kind == "R10G10B10A2" else 3
        if ((kind == "R10G10B10A2" and comp not in ("UInt", "SInt", "UNorm", "SNorm", "UNormSRGB"))
                or (kind == "R11G11B10" and comp != "Float")):
            raise ValueError("UNSUPPORTED_FORMAT: packed component type")
        def unpack(data, offset):
            bits = struct.unpack_from("<I", data, offset)[0]
            if kind == "R11G11B10":
                return [_ufloat(bits & 2047, 6), _ufloat((bits >> 11) & 2047, 6),
                        _ufloat((bits >> 22) & 1023, 5)]
            values = [bits & 1023, (bits >> 10) & 1023, (bits >> 20) & 1023, bits >> 30]
            if comp in ("SInt", "SNorm"):
                values = [v - (1 << w) if v & (1 << (w - 1)) else v for v,w in zip(values,[10,10,10,2])]
            if comp in ("UNorm", "UNormSRGB"):
                return [v / float(m) for v,m in zip(values,[1023,1023,1023,3])]
            if comp == "SNorm":
                return [max(-1.0,v / float(m)) for v,m in zip(values,[511,511,511,1])]
            return values
    else:
        raise ValueError("UNSUPPORTED_FORMAT: %s" % kind)

    def read(data, offset, domain):
        values = unpack(data, offset)
        if fmt.BGRAOrder() and len(values) >= 3:
            values[0], values[2] = values[2], values[0]
        if domain == "linear" and srgb:
            values[:3] = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
                          for v in values[:3]]
        return values
    return size, count, read


def validate_region(region, width, height):
    if not isinstance(region, dict) or set(region) != {"x", "y", "width", "height"}:
        raise ValueError("INVALID_REQUEST: region requires x/y/width/height")
    x, y, w, h = (region[k] for k in ("x", "y", "width", "height"))
    if any(type(v) is not int for v in (x, y, w, h)) or min(x, y) < 0 or min(w, h) < 1:
        raise ValueError("INVALID_REQUEST: invalid ROI coordinates")
    if x + w > width or y + h > height:
        raise ValueError("INVALID_REQUEST: ROI outside mip")
    if w * h > MAX_ROI_PIXELS:
        raise ValueError("RESOURCE_LIMIT: ROI exceeds 262144 pixels")
    return x, y, w, h
