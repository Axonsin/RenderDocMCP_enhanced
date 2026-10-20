from renderdoc import PathEntry
from typing import List


# Synthetic function
def DirectoryBrowseCallback(path: str, entries: List[PathEntry]):
    """
    Not a member function - the signature for any ``DirectoryBrowseCallback`` callbacks.
    
    :param str path: The path that was queried for.
    :param List[renderdoc.PathEntry] entries: The entries underneath the path, as relevant.
    """
    pass

