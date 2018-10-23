# -*- coding: utf-8 -*-
# flake8: noqa
# noreorder
"""
Underscore-to-camelCase converter (and vice versa) for strings and dict keys in Python.
"""
__title__ = 'pyhumps'
__version__ = '1.0.19'
__author__ = 'Nick Ficano'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2018 Nick Ficano'

from humps.humps import camelize
from humps.humps import decamelize
from humps.humps import depascalize
from humps.humps import pascalize

from humps.humps import is_camelcase
from humps.humps import is_pascalcase
from humps.humps import is_snakecase
