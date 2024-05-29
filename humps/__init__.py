# flake8: noqa
# noreorder
"""
Underscore-to-camelCase converter (and vice versa) for strings and dict keys in Python.
"""
__title__ = "pyhumps"
__version__ = "3.8.0"
__author__ = "Nick Ficano"
__license__ = "Unlicense License"
__copyright__ = "Copyright 2019 Nick Ficano"

from humps.main import (
    camelize,
    decamelize,
    kebabize,
    dekebabize,
    pascalize,
    depascalize,
    is_camelcase,
    is_kebabcase,
    is_pascalcase,
    is_snakecase,
)

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
