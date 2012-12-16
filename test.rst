=================
`mathapi` doctest
=================

To test this module, importing is a must.

>>> from mathapi import *

The `import *` is just for convenience, since every items will be tested.

Help from other modules also needed, but not `import *` to prevent collision.

>>> import math
>>> import itertools

Constance
=========

Single Value
------------

>>> pi
3.141592653589793
>>> phi
1.618033988749895

Set of Vaules
-------------

>>> fibonacci
[1, 1, ...]
>>> prime
[2, 3, ...]

This list of value will not growth until we need element beyond the last one.

>>> fibonacci[10]
89
>>> fibonacci
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...]

Prime number works sighly difference, it may produce primes more than expected.

>>> prime[10]
31
>>> prime
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, ...]

Function
========

Prime-Number Relate
-------------------

Prime-Counting Function

>>> [pi(i) for i in range(20)]
[0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8]
>>> pi(100)
25
>>> for i in itertools.count():
...     if pi(i) > 100:
...         print(i)
...         break
... 
547

This is also equalence to

>>> prime[100]
547

To test whether n is prime, use `in` keyword.

>>> 43 in prime
True
>>> 1007 in prime
False

Summation
---------

>>> summation(100)
5050

