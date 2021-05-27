<p align="center">
  <img src="https://raw.githubusercontent.com/nficano/humps/master/artwork/humps.png" alt="Humps logo" width="245" height="118">
</p>

<div align="center">
  <a href="http://humps.readthedocs.io/en/latest/?badge=latest">
    <img src="https://readthedocs.org/projects/humps/badge/?version=latest" />
  </a>
  <a href="https://coveralls.io/github/nficano/humps?branch=master">
    <img src="https://coveralls.io/repos/github/nficano/humps/badge.svg?branch=master#cachebus" />
  </a>
  <a href="https://pypi.org/project/pyhumps/">
    <img src="https://img.shields.io/pypi/v/pyhumps.svg#cachebust" />
  </a>
  <a href="https://pypi.org/project/pyhumps/">
    <img src="https://img.shields.io/pypi/dm/pyhumps.svg" />
  </a>
  <a href="https://pypi.python.org/pypi/pyhumps/">
    <img src="https://img.shields.io/pypi/pyversions/pyhumps.svg" />
  </a>
</div>
</p>

Convert strings (and dictionary keys) between snake case, camel case and pascal case in Python. Inspired by [Humps](https://github.com/domchristie/humps) for Node.

## Jan 11, 2021: An open call for contributors:
Please email me at nficano@gmail.com.

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

# what about abbrevations, acronyms, and initialisms? No problem!
humps.decamelize('APIResponse')  # api_response
```

<hr>

## Humps Cookbook

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
