#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
"""This module contains setup instructions for pyhumps."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('LICENSE') as readme_file:
    license = readme_file.read()


def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


setup(
    name='pyhumps', version='1.0.14', author='Nick Ficano',
    author_email='nficano@gmail.com', packages=['humps'],
    url='https://github.com/nficano/humps', license=license,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console', 'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    description=(
        '🐫  Convert strings (and dictionary keys) between snake case, camel '
        'case and pascal case in Python. Inspired by Humps for Node'
    ),
    long_description_content_type='text/markdown',
    long_description=remove_html_tags(readme), zip_safe=True,
)
