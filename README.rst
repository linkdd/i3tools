i3tools
=======

.. image:: https://img.shields.io/pypi/l/i3tools.svg?style=flat-square
   :target: https://pypi.python.org/pypi/i3tools/
   :alt: License

.. image:: https://img.shields.io/pypi/status/i3tools.svg?style=flat-square
   :target: https://pypi.python.org/pypi/i3tools/
   :alt: Development Status

.. image:: https://img.shields.io/pypi/v/i3tools.svg?style=flat-square
   :target: https://pypi.python.org/pypi/i3tools/
   :alt: Latest release

.. image:: https://img.shields.io/pypi/pyversions/i3tools.svg?style=flat-square
   :target: https://pypi.python.org/pypi/i3tools/
   :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/implementation/i3tools.svg?style=flat-square
   :target: https://pypi.python.org/pypi/i3tools/
   :alt: Supported Python implementations

.. image:: https://img.shields.io/pypi/wheel/i3tools.svg?style=flat-square
   :target: https://travis-ci.org/linkdd/i3tools
   :alt: Download format

.. image:: https://img.shields.io/pypi/dm/i3tools.svg?style=flat-square
   :target: https://pypi.python.org/pypi/i3tools/
   :alt: Downloads

Tools for i3 window manager.

Installation
------------

.. code-block:: text

   pip install i3tools

Usage
-----

i3ws
~~~~

Go to previous/next workspace.

.. code-block:: text

   i3ws <prev|next>

Configuration:

.. code-block:: text

   bindsym $mod+Ctrl+Left exec i3ws prev
   bindsym $mod+Ctrl+Right exec i3ws next
