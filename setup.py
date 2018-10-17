#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module contains setup instructions for pyhumps."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('LICENSE') as readme_file:
    license = readme_file.read()

setup(
    name='pyhumps', version='1.0.0', author='Nick Ficano',
    author_email='nficano@gmail.com', packages=['humps'],
    url='https://github.com/nficano/humps', license=license,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console', 'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English', 'Operating System :: MacOS',
        'Operating System :: Microsoft', 'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python', 'Topic :: Utilities', ],
    description=(
        '🐫  Underscore-to-camelCase converter (and vice versa) for strings '
        'and dict keys in Python.'
    ),
    long_description=readme, zip_safe=True,
)
