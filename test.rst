===================
``mathapi`` Doctest
===================

This doctest also help user learn ``mathapi``'s features.

To experiment with this module, import it first.

>>> from mathapi import *

The ``import *`` is just for convenience, since every items will be tested.

Help from other modules also needed, but not ``import *`` to prevent collision.

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

List of Vaules
--------------

>>> fibonacci
[1, 1, ...]
>>> prime
[2, 3, ...]

The list will not growth until element beyond the last one is needed.

>>> fibonacci[10]
89
>>> fibonacci
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...]

Prime list works sighly difference, it may produce primes more than expected.

>>> prime[5]
13
>>> prime
[2, 3, 5, 7, 11, 13, 17, 19, 23, ...]

Slicing list to get exact number of elements are possible, however.

>>> prime[:12]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

Function
========

Prime-Number Relate
-------------------

Prime-Counting Function ``pi`` (share name with the constance).

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

To test whether n is prime, use ``in`` keyword.

>>> 43 in prime
True
>>> 1007 in prime
False

Factorization with ``factorized``.

>>> factorized(42)
[2, 3, 7]

To get list of all dividable, use ``divisors``.

>>> divisors(42)
[1, 2, 3, 6, 7, 14, 21, 42]

A rought implementation of divisor function, such as sigma_0 and sigma_1.

>>> len(divisors(42)) # sigma_0
8
>>> sum(divisors(42)) # sigma_1
96

``phi``, also known as Euler totient, will show number of relatively primes.

>>> phi(42)
12
>>> phi(43)
42

Working with List of Numbers
----------------------------

``prod`` works like builtin's ``sum``, except each numbers will be multiply.

>>> prod([1, 2, 3, 4, 5])
120

While ``summation`` doesn't takes full list, it require just the last one.
    and assume this list start from 1, with 1 step.

>>> summation(100)
5050
>>> summation(1234567890)
762078938126809995

It's can also power to each number like this

>>> sum(i**2 for i in range(1, 11))
385
>>> summation(10, 2)
385

Meta
====

To create duality value-function data, use ``@duality`` as function decorator.

>>> @duality(1.23456789)
... def geek(n):
...     return 1/n**2 + 1/n
...
>>> geek * 5
6.17283945
>>> geek(9)
0.12345679012345678

This is quite same to infinite list, except you need to ``return locals()``.

>>> @infinitelist([0, 1, 4, 9])
... def sequence(class_base):
...     def __generate__(self):
...         self.append(len(self) ** 2)
...     return locals()
...
>>> sequence
[0, 1, 4, 9, ...]
>>> sequence[10]
100
>>> sequence
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, ...]

The ``__generate__`` method is just for convenience, it will be called when
    element at desire index is not yet create.
