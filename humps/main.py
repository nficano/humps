# -*- coding: utf-8 -*-
"""
This module contains all the core logic for humps.
"""
import re
import sys
from collections import Mapping

_ver = sys.version_info
is_py2 = (_ver[0] == 2)
is_py3 = (_ver[0] == 3)


if is_py2:
    str = unicode  # noqa


if is_py3:
    str = str


UNDERSCORE_RE = re.compile(r'[\-_\s]+(.?)')
SPLIT_RE = re.compile(r'([A-Z][^A-Z]*)')


def pascalize(str_or_iter):
    """Converts a string, dict, or list of dicts to pascal case.

    :param str_or_iter:
      A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: Union[list, dict, str]
    :returns:
      pascalized string, dictionary, or list of dictionaries.

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
    :type str_or_iter: Union[list, dict, str]
    :rtype: Union[list, dict, str]
    :returns:
      camelized string, dictionary, or list of dictionaries.

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
    :type str_or_iter: Union[list, dict, str]
    :rtype: Union[list, dict, str]
    :returns:
      snake cased string, dictionary, or list of dictionaries.

    """
    if str(str_or_iter).isnumeric():
        return str_or_iter
    elif isinstance(str_or_iter, (list, Mapping)):
        return _process_keys(str_or_iter, decamelize)
    else:
        return separate_words(str_or_iter).lower()


def depascalize(str_or_iter):
    """Converts a string, dict, or list of dicts to snake case.

    :param str_or_iter:
      A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: Union[list, dict, str]
    :returns:
      snake cased string, dictionary, or list of dictionaries.

    """
    return decamelize(str_or_iter)


def is_camelcase(str_or_iter):
    """Determines if a string, dict, or list of dicts is camel case.

    :param str_or_iter:
      A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: bool
    :returns:
      True/False whether string or iterable is camel case
    """
    return str_or_iter == camelize(str_or_iter)


def is_pascalcase(str_or_iter):
    """Determines if a string, dict, or list of dicts is pascal case.

    :param str_or_iter:
      A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: bool
    :returns:
      True/False whether string or iterable is pascal case
    """
    return str_or_iter == pascalize(str_or_iter)


def is_snakecase(str_or_iter):
    """Determines if a string, dict, or list of dicts is snake case.

    :param str_or_iter:
      A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: bool
    :returns:
      True/False whether string or iterable is snake case
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
