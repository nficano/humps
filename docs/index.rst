.. humps documentation master file, created by
   sphinx-quickstart on Mon Oct  9 02:11:41 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

humps
======
Release v\ |version|. (:ref:`Installation <install>`)

.. image:: https://img.shields.io/pypi/v/pyhumps.svg
  :alt: Pypi
  :target: https://pypi.python.org/pypi/pyhumps/

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
    >>> humps.decamelize('illWearYourGranddadsClothes')   # 'ill_wear_your_granddads_clothes'
    >>> humps.camelize('i_look_incredible')               # 'iLookIncredible'
    >>> humps.pascalize('im_in_this_big_ass_coat')        # 'ImInThisBigAssCoat'
    >>> humps.decamelize('FROMThatThriftShop')            # 'from_that_thrift_shop'
    >>> humps.decamelize([{'downTheRoad': True}])         # [{'down_the_road': True}]

Features
--------

- Convert from ``snake_case`` to ``camelCase`` and ``PascalCase``
- Convert from ``camelCase`` to ``snake_case`` and ``PascalCase``
- Convert from ``PascalCase`` to  ``snake_case`` and ``camelCase``
- Supports recursively converting ``dict`` keys
- Supports recursively converting lists of dictionaries
- Gracefully handles abbrevations, acronyms, and initialisms
- Extensively documented source code
- No third-party dependencies

Installation
------------

To install humps, simply use pipenv (or pip, of course)::

    $ pipenv install pyhumps

The API Documentation / Guide
-----------------------------

If you are looking for information on a specific function, this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
