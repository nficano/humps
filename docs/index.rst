.. humps documentation master file, created by
   sphinx-quickstart on Mon Oct  9 02:11:41 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

humps
======
Release v\ |version|. (:ref:`Installation <install>`)

.. image:: https://img.shields.io/pypi/v/pyhumps.svg
  :alt: Pypi
  :target: https://pypi.python.org/pypi/humps/

.. image:: https://travis-ci.org/nficano/humps.svg?branch=master
   :alt: Build status
   :target: https://travis-ci.org/nficano/humps

.. image:: https://readthedocs.org/projects/humps/badge/?version=latest
  :target: http://humps.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/nficano/humps/badge.svg?branch=master
  :alt: Coverage
  :target: https://coveralls.io/github/nficano/humps?branch=master

.. image:: https://img.shields.io/pypi/pyversions/pyhumps.svg
  :alt: Python Versions
  :target: https://pypi.python.org/pypi/pyhumps/

**humps**  🐫 Convert strings (and dictionary keys) between snake case, camel case and pascal case in Python. Inspired by Humps for Node

-------------------

**Introducing Humps for Python! Let's see it in action**::

    >>> import humps
    >>> humps.camelize('jack_in_the_box')  # jackInTheBox
    >>> humps.decamelize('rubyTuesdays')  # ruby_tuesdays
    >>> humps.pascalize('red_robin')  # RedRobin
    >>> humps.decamelize('APIResponse')  # api_response
    >>> humps.decamelize([{'attrOne': 'foo'}, {'attrOne': 'bar'}]) # [{'attr_one': 'foo'}, {'attr_one': 'bar'}]


Features
--------

- Convert from snake_case to camelcase and pascal case
- Convert from camelcase to snake_case and pascal case
- Convert from pascal case to camelcase and snake_case
- Supports strings
- Supports recursively converting dictionary keys
- Supports recursively converting lists of dictionaries
- Gracefully handles abbrevations and acronyms
- Includes functions to test if a string, dict, or list of dicts is camelcase, snake_case, and pascal case.
- Extensively Documented Source Code
- No Third-Party Dependencies

Installation
------------

To install humps, simply use pipenv (or pip, of course)::

    $ pipenv install pyhumps

The API Documentation / Guide
-----------------------------

If you are looking for information on a specific function, class, or method, this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
