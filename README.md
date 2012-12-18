Math API
========

Digging into <http://projecteuler.net>, I discover many interesting
mathematical technique, which not yet include in main. So I write it out.

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
- Number Theory
    - `factorized`: Prime factorization of a number.
    - `divisors`: Show all positive divisable numbers of a number.
    - `Fraction.decimal`: Show repeating decimal of a fraction number.
- Arithmetic Function
    - `prod`: Production of a list of numbers.
    - `summation`: Summation of numbers from `[1..n]`, or `[1**p..n**p]`.

See document in file [test.rst](./test.rst)

Installation
------------

Download source and, as root

    python setup.py install

