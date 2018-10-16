<p align="center">
  <img src="./artwork/humps.png" alt="Humps logo" width="245" height="118">
  <div align="center">
    <a href="https://travis-ci.org/nficano/humps"><img src="https://travis-ci.org/nficano/humps.svg?branch=master" /></a>
    <a href="https://coveralls.io/repos/github/nficano/humps/badge.svg?branch=master"><img src="https://coveralls.io/github/nficano/humps?branch=master" /></a>
    <a href="https://pypi.org/project/pyhumps/"><img src="https://img.shields.io/pypi/v/pyhumps.svg" alt="pypi"></a>
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
humps.decamelize_keys(array) # [{'attr_one': 'foo'}, {'attr_one': 'bar'}]

array = [{'attr_one': 'foo'}, {'attr_one': 'bar'}]
humps.camelize_keys(array)  # [{'attrOne': 'foo'}, {'attrOne': 'bar'}]

array = [{'attr_one': 'foo'}, {'attr_one': 'bar'}]
humps.pascalize_keys(array)  # [{'AttrOne': 'foo'}, {'AttrOne': 'bar'}]
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

### How personally I use humps

#### Pythonic Boto3 API Wrapper

```python
# aws.py
import humps
import boto3

def api(service, decamelize=True, *args, **kwargs):
    service, func = service.split(':')
    client = boto3.client(service)
    kwargs = humps.pascalize_keys(kwargs)
    response = getattr(client, func)(*args, **kwargs)
    return (depascalize_keys(response) if decamelize else response)

api('s3:download_file', bucket='bucket', key='hello.png', filename='hello.png')
```

#### Flask-RESTful Adaptive responses

```python
# I will post a code snippet for this soon. It's a decorator that checks if
# the request was arguments were passed as camelcase or snake_case, it then
# rewrites the response to match the consumer's preferred casing style.
```
