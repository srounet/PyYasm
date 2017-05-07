pyyasm
======
.. image:: https://coveralls.io/repos/github/srounet/PyYasm/badge.svg?branch=master
  :target: https://coveralls.io/github/srounet/PyYasm?branch=master
Python x86/x64 wrapper for Yasm

Using pyyasm
============

.. code-block:: python

    import pyyasm
    
    # some inline asm which does nothing just to show how the library works
    # __asm as to be bytes.
    __asm = b"""
	    use32
	    org 0
        pushfd
        pushad
        popad
        popfd
    """
    bytecode = pyyasm.assemble(__asm)
    print(bytecode)
    
    > b'f\x9cf`faf\x9d'


Running tests
=============

.. code-block:: shell

    python setup.py test

Changelog
=========

0.0.1: initial release (07/05/2017)
