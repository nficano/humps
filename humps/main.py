"""
This module contains all the core logic for humps.
"""
import re

from collections.abc import Mapping

ACRONYM_RE = re.compile(r"([A-Z\d]+)(?=[A-Z\d]|$)")
PASCAL_RE = re.compile(r"([^\-_]+)")
SPLIT_RE = re.compile(r"([\-_]*[A-Z][^A-Z]*[\-_]*)")
UNDERSCORE_RE = re.compile(r"(?<=[^\-_])[\-_]+[^\-_]")


def pascalize(str_or_iter):
    """
    Convert a string, dict, or list of dicts to pascal case.

    :param str_or_iter:
        A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: Union[list, dict, str]
    :returns:
        pascalized string, dictionary, or list of dictionaries.
    """
    if isinstance(str_or_iter, (list, Mapping)):
        return _process_keys(str_or_iter, pascalize)

    s = _is_none(str_or_iter)
    if s.isupper() or s.isnumeric():
        return str_or_iter

    def _replace_fn(match):
        """
        :rtype: str
        """
        return match.group(1)[0].upper() + match.group(1)[1:]

    s = camelize(PASCAL_RE.sub(_replace_fn, s))
    return s[0].upper() + s[1:] if len(s) != 0 else s


def camelize(str_or_iter):
    """
    Convert a string, dict, or list of dicts to camel case.

    :param str_or_iter:
        A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: Union[list, dict, str]
    :returns:
        camelized string, dictionary, or list of dictionaries.
    """
    if isinstance(str_or_iter, (list, Mapping)):
        return _process_keys(str_or_iter, camelize)

    s = _is_none(str_or_iter)
    if s.isupper() or s.isnumeric():
        return str_or_iter

    if len(s) != 0 and not s[:2].isupper():
        s = s[0].lower() + s[1:]

    # For string "hello_world", match will contain
    #             the regex capture group for "_w".
    return UNDERSCORE_RE.sub(lambda m: m.group(0)[-1].upper(), s)


def kebabize(str_or_iter):
    """
    Convert a string, dict, or list of dicts to kebab case.
    :param str_or_iter:
        A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: Union[list, dict, str]
    :returns:
        kebabized string, dictionary, or list of dictionaries.
    """
    if isinstance(str_or_iter, (list, Mapping)):
        return _process_keys(str_or_iter, kebabize)

    s = _is_none(str_or_iter)
    if s.isnumeric():
        return str_or_iter

    if not (s.isupper()) and (is_camelcase(s) or is_pascalcase(s)):
        return (
            _separate_words(
                string=_fix_abbreviations(s),
                separator="-"
            ).lower()
        )

    return UNDERSCORE_RE.sub(lambda m: "-" + m.group(0)[-1], s)


def decamelize(str_or_iter):
    """
    Convert a string, dict, or list of dicts to snake case.

    :param str_or_iter:
        A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: Union[list, dict, str]
    :returns:
        snake cased string, dictionary, or list of dictionaries.
    """
    if isinstance(str_or_iter, (list, Mapping)):
        return _process_keys(str_or_iter, decamelize)

    s = _is_none(str_or_iter)
    if s.isupper() or s.isnumeric():
        return str_or_iter

    return _separate_words(_fix_abbreviations(s)).lower()


def depascalize(str_or_iter):
    """
    Convert a string, dict, or list of dicts to snake case.

    :param str_or_iter: A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: Union[list, dict, str]
    :returns:
        snake cased string, dictionary, or list of dictionaries.
    """
    return decamelize(str_or_iter)


def dekebabize(str_or_iter):
    """
    Convert a string, dict, or list of dicts to snake case.
    :param str_or_iter:
        A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: Union[list, dict, str]
    :returns:
        snake cased string, dictionary, or list of dictionaries.
    """
    if isinstance(str_or_iter, (list, Mapping)):
        return _process_keys(str_or_iter, dekebabize)

    s = _is_none(str_or_iter)
    if s.isnumeric():
        return str_or_iter

    return s.replace("-", "_")


def is_camelcase(str_or_iter):
    """
    Determine if a string, dict, or list of dicts is camel case.

    :param str_or_iter:
        A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: bool
    :returns:
        True/False whether string or iterable is camel case
    """
    return str_or_iter == camelize(str_or_iter)


def is_pascalcase(str_or_iter):
    """
    Determine if a string, dict, or list of dicts is pascal case.

    :param str_or_iter: A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: bool
    :returns:
        True/False whether string or iterable is pascal case
    """
    return str_or_iter == pascalize(str_or_iter)


def is_kebabcase(str_or_iter):
    """
    Determine if a string, dict, or list of dicts is camel case.
    :param str_or_iter:
        A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: bool
    :returns:
        True/False whether string or iterable is camel case
    """
    return str_or_iter == kebabize(str_or_iter)


def is_snakecase(str_or_iter):
    """
    Determine if a string, dict, or list of dicts is snake case.

    :param str_or_iter:
        A string or iterable.
    :type str_or_iter: Union[list, dict, str]
    :rtype: bool
    :returns:
        True/False whether string or iterable is snake case
    """
    if is_kebabcase(str_or_iter) and not is_camelcase(str_or_iter):
        return False

    return str_or_iter == decamelize(str_or_iter)


def _is_none(_in):
    """
    Determine if the input is None
    and returns a string with white-space removed
    :param _in: input
    :return:
        an empty sting if _in is None,
        else the input is returned with white-space removed
    """
    return "" if _in is None else re.sub(r"\s+", "", str(_in))


def _process_keys(str_or_iter, fn):
    if isinstance(str_or_iter, list):
        return [_process_keys(k, fn) for k in str_or_iter]
    if isinstance(str_or_iter, Mapping):
        return {fn(k): _process_keys(v, fn) for k, v in str_or_iter.items()}
    return str_or_iter


def _fix_abbreviations(string):
    """
    Rewrite incorrectly cased acronyms, initialisms, and abbreviations,
    allowing them to be decamelized correctly. For example, given the string
    "APIResponse", this function is responsible for ensuring the output is
    "api_response" instead of "a_p_i_response".

    :param string: A string that may contain an incorrectly cased abbreviation.
    :type string: str
    :rtype: str
    :returns:
        A rewritten string that is safe for decamelization.
    """
    return ACRONYM_RE.sub(lambda m: m.group(0).title(), string)


def _separate_words(string, separator="_"):
    """
    Split words that are separated by case differentiation.
    :param string: Original string.
    :param separator: String by which the individual
        words will be put back together.
    :returns:
        New string.
    """
    return separator.join(s for s in SPLIT_RE.split(string) if s)
