"PyDEC meshes"

from .generation import *
from .ncube import *
from .regular_cube import *
from .simplex import *
from .subdivision import *

__all__ = list(filter(lambda s: not s.startswith('_'), dir()))

# TODO: replace testing framework with pytest (?) since Tester is deprecated
# from pydec.testing import Tester
# test = Tester().test
