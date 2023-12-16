"PyDEC mesh and array IO"

from .arrayio import *
from .meshio import *

__all__ = list(filter(lambda s: not s.startswith('_'), dir()))
