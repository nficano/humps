"""This module contains setup instructions for pyhumps."""
import codecs
import os

import setuptools

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setuptools.setup(
    name="pyhumps",
    version="3.5.2",
    author="Nick Ficano",
    author_email="nficano@gmail.com",
    packages=["humps"],
    package_data={"": ["LICENSE"], "humps": ["py.typed", "main.pyi"]},
    url="https://github.com/nficano/humps",
    license="The Unlicense (Unlicense)",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    description=(
        "🐫  Convert strings (and dictionary keys) between snake case, camel "
        "case and pascal case in Python. Inspired by Humps for Node"
    ),
    include_package_data=True,
    long_description_content_type="text/markdown",
    long_description=long_description,
    keywords=["humps", "snakecase", "convert case", "camelcase"],
)
