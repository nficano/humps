<p align="center">
  <img src="https://raw.githubusercontent.com/nficano/humps/master/artwork/humps.png" alt="Humps logo" width="245" height="118">
  <div align="center">
    <a href="https://travis-ci.org/nficano/humps"><img src="https://travis-ci.org/nficano/humps.svg?branch=master" /></a>
    <a href="https://coveralls.io/github/nficano/humps?branch=master"><img src="https://coveralls.io/repos/github/nficano/humps/badge.svg?branch=master#cachebust" /></a>
    <a href="https://pypi.org/project/pyhumps/"><img src="https://img.shields.io/pypi/v/pyhumps.svg#cachebust" alt="pypi"></a>
    <a href="https://pypi.python.org/pypi/pyhumps/"><img src="https://img.shields.io/pypi/pyversions/pyhumps.svg" /></a>
  </div>
</p>


Convert strings (and dictionary keys) between snake case, camel case and pascal case in Python. Inspired by [Humps](https://github.com/domchristie/humps) for Node.

## Why

When creating an API, the authors will often use the character casing convention that is idiomatic to their backend language, thus forcing consumers developing in a different language (with different style guidelines) to tolerate inconsistent casing styles, hardcode mappings between the two, or lug around some case conversion utility functions.

While none of these are inherently wrong, it would still be nice to have a dependable solution just a few keystrokes away.

## Installation

To install humps, simply use pipenv (or pip, of course):

```bash
$ pipenv install pyhumps
```

## Usage

### Converting strings

```python
import humps

humps.camelize('jack_in_the_box')  # jackInTheBox
humps.decamelize('rubyTuesdays')  # ruby_tuesdays
humps.pascalize('red_robin')  # RedRobin
```

### Converting dictionary keys

```python
import humps

array = [{'attrOne': 'foo'}, {'attrOne': 'bar'}]
humps.decamelize(array) # [{'attr_one': 'foo'}, {'attr_one': 'bar'}]

array = [{'attr_one': 'foo'}, {'attr_one': 'bar'}]
humps.camelize(array)  # [{'attrOne': 'foo'}, {'attrOne': 'bar'}]

array = [{'attr_one': 'foo'}, {'attr_one': 'bar'}]
humps.pascalize(array)  # [{'AttrOne': 'foo'}, {'AttrOne': 'bar'}]
```

### Checking character casing
```python
import humps

humps.is_camelcase('illWearYourGranddadsClothes')  # True
humps.is_pascalcase('ILookIncredible')  # True
humps.is_snakecase('im_in_this_big_ass_coat')  # True
humps.is_camelcase('from_that_thrift_shop')  # False
humps.is_snakecase('downTheRoad')  # False
```

<hr>

### My Recipes

#### Pythonic Boto3 API Wrapper

```python
# aws.py
import humps
import boto3

def api(service, decamelize=True, *args, **kwargs):
    service, func = service.split(':')
    client = boto3.client(service)
    kwargs = humps.pascalize(kwargs)
    response = getattr(client, func)(*args, **kwargs)
    return (depascalize(response) if decamelize else response)

# usage
api('s3:download_file', bucket='bucket', key='hello.png', filename='hello.png')
```


#### API Wrapper Returning Decorator

```python
from functools import wraps
import enum

import humps


class Flags(enum.Enum):
    RAW = 1
    JSON = 2
    STATUS_CODE = 4
    OK = 8
    DECAMELIZE = 16


def returning(api_exception=Exception):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            flags = []
            if 'returning' in kwargs:
                returning = kwargs.pop('returning')
                if isinstance(returning, Flags):
                    flags.append(returning)
                else:
                    flags.extend(returning)
            flags.extend([a for a in args if isinstance(a, Flags)])
            args = [a for a in args if not isinstance(a, Flags)]
            resp = fn(*args, **kwargs)
            is_json = resp.headers.get('Content-Type') == 'application/json'
            if not flags or Flags.RAW in flags:
                return resp
            if Flags.OK in flags:
                return resp.ok
            if Flags.STATUS_CODE in flags:
                return resp.status_code
            if Flags.JSON in flags:
                if not resp.ok:
                    raise api_exception(resp.json() if is_json else resp.text)
                if Flags.DECAMELIZE in flags:
                    return humps.decamelize(resp.json())
                else:
                    return resp.json()
        return wrapper
    return decorator

# usage
import requests

@returning()
def get_todo(todo_id):
  return requests.get('https://jsonplaceholder.typicode.com/posts/1')

get_todo(1) # <Response [200]> (unaltered response object)

get_todo(1, Flags.JSON) # {'userId': 1, 'id': 1, 'title': '...'}

get_todo(1, Flags.JSON, Flags.DECAMELIZE) # {'user_id': 1, 'id': 1, 'title': '...'}

get_todo(1, Flags.OK) # True

get_todo(1, Flags.STATUS_CODE) # 200
```


#### Flask-RESTful Adaptive Responses

```python
# I will post a code snippet for this soon. It's a decorator that checks if
# the request arguments were passed as camelcase or snake_case, it then
# rewrites the response to match the consumer's preferred casing style.
```
