# flake8: noqa
# noreorder
"""
Underscore-to-camelCase converter (and vice versa) for strings and dict keys in Python.
"""
import sys

from humps.main import (camelize, decamelize, dekebabize, depascalize,
                        is_camelcase, is_kebabcase, is_pascalcase,
                        is_snakecase, kebabize, pascalize)

if sys.version_info >= (3, 8):  # pragma: no cover
    from importlib.metadata import metadata as _importlib_metadata
else:
    from importlib_metadata import metadata as _importlib_metadata  # pragma: no cover

__title__ = "pyhumps"
__version__ = _importlib_metadata(__title__)["version"]
__author__ = "Nick Ficano"
__license__ = "Unlicense License"
__copyright__ = "Copyright 2019 Nick Ficano"

__all__ = (
    "camelize",
    "decamelize",
    "kebabize",
    "dekebabize",
    "pascalize",
    "depascalize",
    "is_camelcase",
    "is_kebabcase",
    "is_pascalcase",
    "is_snakecase",
)
