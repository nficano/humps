# -*- coding: utf-8 -*-
# flake8: noqa
# noreorder
"""
Underscore-to-camelCase converter (and vice versa) for strings and dict keys in Python.
"""
__title__ = "pyhumps"
__version__ = "1.6.1"
__author__ = "Nick Ficano"
__license__ = "MIT License"
__copyright__ = "Copyright 2019 Nick Ficano"

from humps.main import camelize
from humps.main import decamelize
from humps.main import depascalize
from humps.main import pascalize

from humps.main import is_camelcase
from humps.main import is_pascalcase
from humps.main import is_snakecase
