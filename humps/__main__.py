import re
from collections import Mapping

UNDERSCORE_RE = re.compile('[\-_\s]+(.?)')
SPLIT_RE = re.compile('([A-Z][^A-Z]*)')


def _process_keys(obj, fn):
    if isinstance(obj, list):
        return [_process_keys(k, fn) for k in obj]
    elif isinstance(obj, Mapping):
        return {fn(k): _process_keys(v, fn) for k, v in obj.items()}
    else:
        return obj


def separate_words(string, separator='_', split=SPLIT_RE):
    return separator.join([s for s in SPLIT_RE.split(string) if s != ''])


def camelize_keys(obj):
    return _process_keys(obj, camelize)


def camelize(string):
    if string.isnumeric():
        return string
    return ''.join([
        string[0].lower(),
        UNDERSCORE_RE.sub(lambda m: m.group(1).upper(), string)[1:],
    ])


def decamelize_keys(obj):
    return _process_keys(obj, decamelize)


def decamelize(string):
    return separate_words(string).lower()


def depascalize_keys(obj):
    return _process_keys(obj, decamelize)


def depascalize(string):
    return decamelize(string)


def is_camelcase(string):
    return string == camelize(string)


def is_pascalcase(string):
    return string == pascalize(string)


def is_snakecase(string):
    return string == decamelize(string)


def pascalize_keys(obj):
    return _process_keys(obj, pascalize)


def pascalize(string):
    return ''.join([string[0].upper(), camelize(string[1:])])
