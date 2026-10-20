from enum import IntEnum

class Visualisation(IntEnum):
    # Original docstring
    """
    What kind of visualisation to use when rendering a mesh.
    
    .. data:: NoSolid
    
      No solid shading should be done.
    
    .. data:: Solid
    
      The mesh should be rendered in a single flat unshaded color.
    
    .. data:: Lit
    
      The mesh should be rendered with face normals generated on the primitives and used for lighting.
    
    .. data:: Secondary
    
      The mesh should be rendered using the secondary element as color.
    
    .. data:: Explode
    
      The mesh should be rendered with vertices displaced and coloured by vertex ID.
    
    .. data:: Meshlet
    
      The mesh should be rendered colorising each meshlet differently.
    """
    
    
    # Enum values
    
    NoSolid = 0
    """
    No solid shading should be done.
    """
    
    Solid = 1
    """
    The mesh should be rendered in a single flat unshaded color.
    """
    
    Lit = 2
    """
    The mesh should be rendered with face normals generated on the primitives and used for lighting.
    """
    
    Secondary = 3
    """
    The mesh should be rendered using the secondary element as color.
    """
    
    Explode = 4
    """
    The mesh should be rendered with vertices displaced and coloured by vertex ID.
    """
    
    Meshlet = 5
    """
    The mesh should be rendered colorising each meshlet differently.
    """
    
    Count = 6
    """
    The number of values in the enum, for ease of iteration.
    """
    

# Assign __doc__ for enum values for easier introspection

Visualisation.NoSolid.__doc__ = """
No solid shading should be done.
"""

Visualisation.Solid.__doc__ = """
The mesh should be rendered in a single flat unshaded color.
"""

Visualisation.Lit.__doc__ = """
The mesh should be rendered with face normals generated on the primitives and used for lighting.
"""

Visualisation.Secondary.__doc__ = """
The mesh should be rendered using the secondary element as color.
"""

Visualisation.Explode.__doc__ = """
The mesh should be rendered with vertices displaced and coloured by vertex ID.
"""

Visualisation.Meshlet.__doc__ = """
The mesh should be rendered colorising each meshlet differently.
"""

Visualisation.Count.__doc__ = """
The number of values in the enum, for ease of iteration.
"""

