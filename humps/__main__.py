import re
from collections import Mapping

from humps.compat import str


UNDERSCORE_RE = re.compile(r'[\-_\s]+(.?)')
SPLIT_RE = re.compile(r'([A-Z][^A-Z]*)')


def pascalize(obj):
    if isinstance(obj, (list, Mapping)):
        return _process_keys(obj, pascalize)
    else:
        return ''.join([obj[0].upper(), camelize(obj[1:])])


def camelize(obj):
    if str(obj).isnumeric():
        return obj
    elif isinstance(obj, (list, Mapping)):
        return _process_keys(obj, camelize)
    else:
        return ''.join([
            obj[0].lower(),
            UNDERSCORE_RE.sub(lambda m: m.group(1).upper(), obj)[1:],
        ])


def decamelize(obj):
    if isinstance(obj, (list, Mapping)):
        return _process_keys(obj, decamelize)
    else:
        return separate_words(obj).lower()


def depascalize(string):
    return decamelize(string)


def is_camelcase(string):
    return string == camelize(string)


def is_pascalcase(string):
    return string == pascalize(string)


def is_snakecase(string):
    return string == decamelize(string)


def _process_keys(obj, fn):
    if isinstance(obj, list):
        return [_process_keys(k, fn) for k in obj]
    elif isinstance(obj, Mapping):
        return {fn(k): _process_keys(v, fn) for k, v in obj.items()}
    else:
        return obj


def separate_words(string, separator='_', split=SPLIT_RE):
    return separator.join([s for s in SPLIT_RE.split(string) if s != ''])
