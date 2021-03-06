Extended Math
=============

`extmath` (formerly `mathapi`) aims to provide a lightweight & independent
extended mathematical module for Python 3.


Avalable Feature
----------------

- Infinite Number Sets
    - `prime`: 2, 3, 5, 7, 11, 13, 17, ...
        - primary test done by asking does element exists, e.g. `13 in prime`.
    - `fibonacci`: 1, 1, 2, 3, 5, 8, 13, 21, ...
        - Compute fibonacci number at any index by `fibonacci(i)`.
            It's the same as `fibonacci[i]`, except the list will not growth.
- Duality Value-Function Data Type
    - `pi`: 3.1416..., or prime-counting function.
    - `phi`: 1.6180..., or Euler's totient function.
- Subscriptable Function
    - `sigma`: divisor function, `sigma[0]` for len and `sigma[1]` for sum.
- Number Theory
    - `factorized`: Prime factorization of a number.
    - `divisors`: Show all positive divisable numbers of a number.
    - `Fraction.decimal`: Show repeating decimal of a fraction number.
- Arithmetic Function
    - `product`: Production of a list of numbers.
    - `sumpow`: Summation of numbers from `[1..n]`, or `[1**p..n**p]`.
    - `sumexp`: Summation of numbers from `[r**0..r**k]`.

See document in file `test.rst`


Installation
------------

    pip install extmath
