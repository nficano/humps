# -*- coding: utf-8 -*-
"""
This module contains all the core logic for humps.
"""
import re
from collections import Mapping

from humps.compat import str


UNDERSCORE_RE = re.compile(r'[\-_\s]+(.?)')
SPLIT_RE = re.compile(r'([A-Z][^A-Z]*)')


def pascalize(str_or_iter):
    """Converts a string, dict, or list of dicts to pascal case.

    :param str_or_iter:
      A string or iterable.

    """
    if str(str_or_iter).isnumeric():
        return str_or_iter
    elif isinstance(str_or_iter, (list, Mapping)):
        return _process_keys(str_or_iter, pascalize)
    else:
        return ''.join([str_or_iter[0].upper(), camelize(str_or_iter[1:])])


def camelize(str_or_iter):
    """Converts a string, dict, or list of dicts to camel case.

    :param str_or_iter:
      A string or iterable.

    """
    if str(str_or_iter).isnumeric():
        return str_or_iter
    elif isinstance(str_or_iter, (list, Mapping)):
        return _process_keys(str_or_iter, camelize)
    else:
        return ''.join([
            str_or_iter[0].lower(),
            UNDERSCORE_RE.sub(lambda m: m.group(1).upper(), str_or_iter)[1:],
        ])


def decamelize(str_or_iter):
    """Converts a string, dict, or list of dicts to snake case.

    :param str_or_iter:
      A string or iterable.

    """
    if str(str_or_iter).isnumeric():
        return str_or_iter
    elif isinstance(str_or_iter, (list, Mapping)):
        return _process_keys(str_or_iter, decamelize)
    else:
        return separate_words(str_or_iter).lower()


def depascalize(string):
    """Converts a string, dict, or list of dicts to snake case.

    :param str_or_iter:
      A string or iterable.

    """
    return decamelize(string)


def is_camelcase(str_or_iter):
    """Determines if a string, dict, or list of dicts is camel case.

    :param str_or_iter:
      A string or iterable.

    """
    return str_or_iter == camelize(str_or_iter)


def is_pascalcase(str_or_iter):
    """Determines if a string, dict, or list of dicts is pascal case.

    :param str_or_iter:
      A string or iterable.

    """
    return str_or_iter == pascalize(str_or_iter)


def is_snakecase(str_or_iter):
    """Determines if a string, dict, or list of dicts is snake case.

    :param str_or_iter:
      A string or iterable.

    """
    return str_or_iter == decamelize(str_or_iter)


def _process_keys(str_or_iter, fn):
    if isinstance(str_or_iter, list):
        return [_process_keys(k, fn) for k in str_or_iter]
    elif isinstance(str_or_iter, Mapping):
        return {fn(k): _process_keys(v, fn) for k, v in str_or_iter.items()}
    else:
        return str_or_iter


def separate_words(string, separator='_', split=SPLIT_RE):
    return separator.join([s for s in SPLIT_RE.split(string) if s != ''])
