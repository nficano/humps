.. _quickstart:

Quickstart
==========

This guide will walk you through the basic usage of humps.

Let's get started with some examples.

Converting strings
------------------

Begin by importing humps::

    >>> import humps

    >>> humps.camelize('jack_in_the_box')  # jackInTheBox
    >>> humps.decamelize('rubyTuesdays')  # ruby_tuesdays
    >>> humps.pascalize('red_robin')  # RedRobin
