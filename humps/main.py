# -*- coding: utf-8 -*-
"""
This module contains all the core logic for humps.
"""
import re
import sys

try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping


_ver = sys.version_info
is_py2 = _ver[0] == 2
is_py3 = _ver[0] == 3

if is_py2:  # pragma: no cover
    str = unicode  # noqa

if is_py3:  # pragma: no cover
    str = str

ACRONYM_RE = re.compile(r"([A-Z]+)(?=[A-Z][a-z])")
PASCAL_RE = re.compile(r"([^\-_\s]+)")
SPLIT_RE = re.compile(r"([\-_\s]*[A-Z0-9]+[^A-Z\-_\s]+[\-_\s]*)")
UNDERSCORE_RE = re.compile(r"([^\-_\s])[\-_\s]+([^\-_\s])")


def pascalize(str_or_iter):
    """Convert a string, dict, or list of dicts to pascal case.

    :param str_or_iter:
      A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: Union[list, dict, str]
    :returns:
      pascalized string, dictionary, or list of dictionaries.

    """
    if isinstance(str_or_iter, (list, Mapping)):
        return _process_keys(str_or_iter, pascalize)

    s = str(str_or_iter)
    if s.isnumeric():
        return str_or_iter

    if s.isupper():
        return str_or_iter

    s = camelize(
        PASCAL_RE.sub(lambda m: m.group(1)[0].upper() + m.group(1)[1:], s),
    )
    return s[0].upper() + s[1:]


def camelize(str_or_iter):
    """Convert a string, dict, or list of dicts to camel case.

    :param str_or_iter:
      A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: Union[list, dict, str]
    :returns:
      camelized string, dictionary, or list of dictionaries.

    """
    if isinstance(str_or_iter, (list, Mapping)):
        return _process_keys(str_or_iter, camelize)

    s = str(str_or_iter)
    if s.isnumeric():
        return str_or_iter

    if s.isupper():
        return str_or_iter

    return "".join(
        [
            s[0].lower() if not s[:2].isupper() else s[0],
            UNDERSCORE_RE.sub(
                lambda m: m.group(1) + m.group(2).upper(), s[1:]
            ),
        ]
    )


def decamelize(str_or_iter):
    """Convert a string, dict, or list of dicts to snake case.

    :param str_or_iter:
      A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: Union[list, dict, str]
    :returns:
      snake cased string, dictionary, or list of dictionaries.

    """
    if isinstance(str_or_iter, (list, Mapping)):
        return _process_keys(str_or_iter, decamelize)

    s = str(str_or_iter)
    if s.isnumeric():
        return str_or_iter

    if s.isupper():
        return str_or_iter

    return separate_words(_fix_abbrevations(s)).lower()


def depascalize(str_or_iter):
    """Convert a string, dict, or list of dicts to snake case.

    :param str_or_iter:
      A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: Union[list, dict, str]
    :returns:
      snake cased string, dictionary, or list of dictionaries.

    """
    return decamelize(str_or_iter)


def is_camelcase(str_or_iter):
    """Determine if a string, dict, or list of dicts is camel case.

    :param str_or_iter:
      A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: bool
    :returns:
      True/False whether string or iterable is camel case
    """
    return str_or_iter == camelize(str_or_iter)


def is_pascalcase(str_or_iter):
    """Determine if a string, dict, or list of dicts is pascal case.

    :param str_or_iter:
      A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: bool
    :returns:
      True/False whether string or iterable is pascal case
    """
    return str_or_iter == pascalize(str_or_iter)


def is_snakecase(str_or_iter):
    """Determine if a string, dict, or list of dicts is snake case.

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


def _fix_abbrevations(string):
    """Rewrite incorrectly cased acronyms, initialisms, and abbrevations,
    allowing them to be decamelized correctly. For example, given the string
    "APIReponse", this function is responsible for ensuring the output is
    "api_response" instead of "a_p_i_response".

    :param str string:
        A string that may contain an incorrectly cased abbrevation.
    :rtype: str
    :returns:
        A rewritten string that is safe for decamelization.
    """
    return ACRONYM_RE.sub(lambda m: m.group(0).title(), string)


def separate_words(string, separator="_", split=SPLIT_RE.split):
    return separator.join(s for s in split(string) if s)
