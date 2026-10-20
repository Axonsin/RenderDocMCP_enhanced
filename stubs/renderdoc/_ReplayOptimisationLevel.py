from enum import IntEnum

class ReplayOptimisationLevel(IntEnum):
    # Original docstring
    """
    The level of optimisation used in
    
    .. data:: NoOptimisation
    
      Completely disabled, no optimisation will be used at all.
    
    .. data:: Conservative
    
      Optimisation is used when it doesn't interfere with replay correctness.
    
    .. data:: Balanced
    
      Optimisation is used when it has minimal impact on replay correctness. This could include e.g.
      resources appearing cleared instead of containing contents from prior frames where those resources
      are written to before being read.
    
    .. data:: Fastest
    
      All possible optimisations are enabled as long as they do not cause invalid/incorrect replay.
      This could result in side-effects like data from one replay being visible early in another replay,
      if it's known that the data will be overwritten before being used.
    """
    
    
    # Enum values
    
    NoOptimisation = 0
    """
    Completely disabled, no optimisation will be used at all.
    """
    
    Conservative = 1
    """
    Optimisation is used when it doesn't interfere with replay correctness.
    """
    
    Balanced = 2
    """
    Optimisation is used when it has minimal impact on replay correctness. This could include e.g.
    resources appearing cleared instead of containing contents from prior frames where those resources
    are written to before being read.
    """
    
    Fastest = 3
    """
    All possible optimisations are enabled as long as they do not cause invalid/incorrect replay.
    This could result in side-effects like data from one replay being visible early in another replay,
    if it's known that the data will be overwritten before being used.
    """
    
    Count = 4
    """
    The number of values in the enum, for ease of iteration.
    """
    
    # Aliases
    
    First = 0
    """
    The first enum value, for ease of iteration.
    """
    

# Assign __doc__ for enum values for easier introspection

ReplayOptimisationLevel.NoOptimisation.__doc__ = """
Completely disabled, no optimisation will be used at all.
"""

ReplayOptimisationLevel.Conservative.__doc__ = """
Optimisation is used when it doesn't interfere with replay correctness.
"""

ReplayOptimisationLevel.Balanced.__doc__ = """
Optimisation is used when it has minimal impact on replay correctness. This could include e.g.
resources appearing cleared instead of containing contents from prior frames where those resources
are written to before being read.
"""

ReplayOptimisationLevel.Fastest.__doc__ = """
All possible optimisations are enabled as long as they do not cause invalid/incorrect replay.
This could result in side-effects like data from one replay being visible early in another replay,
if it's known that the data will be overwritten before being used.
"""

ReplayOptimisationLevel.Count.__doc__ = """
The number of values in the enum, for ease of iteration.
"""

ReplayOptimisationLevel.First.__doc__ = """
The first enum value, for ease of iteration.
"""

