.. _install:

Installation of humps
======================

This part of the documentation covers the installation of humps.

To install humps, simply use pipenv (or pip, of course)::

    $ pipenv install humps

Get the Source Code
-------------------

humps is actively developed on GitHub, where the source is `available <https://github.com/nficano/humps>`_.

You can either clone the public repository::

    $ git clone git://github.com/nficano/humps.git

Or, download the `tarball <https://github.com/nficano/humps/tarball/master>`_::

    $ curl -OL https://github.com/nficano/humps/tarball/master
    # optionally, zipball is also available (for Windows users).

Once you have a copy of the source, you can embed it in your Python package, or install it into your site-packages by running::

    $ cd humps
    $ pipenv install .
