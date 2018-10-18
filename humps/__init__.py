# -*- coding: utf-8 -*-
# flake8: noqa
# noreorder
"""
Underscore-to-camelCase converter (and vice versa) for strings and dict keys in Python.
"""
__title__ = 'pyhumps'
__version__ = '1.0.16'
__author__ = 'Nick Ficano'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2018 Nick Ficano'

from humps.__main__ import camelize
from humps.__main__ import decamelize
from humps.__main__ import depascalize
from humps.__main__ import pascalize

from humps.__main__ import is_camelcase
from humps.__main__ import is_pascalcase
from humps.__main__ import is_snakecase
