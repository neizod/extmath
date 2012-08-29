from functools import reduce
from itertools import product as cartesian_product

def prod(l):
    '''prod(iterable) -> value'''

    return reduce(lambda x, y: x*y, l)

def factorized(n):
    '''factorized(number) -> list

    Prime fatorization of the number, e.g. factorized(42) -> [2, 3, 7]
    Returns empty list if 'n' is 0, or [1] if 'n' is 1 (by defination).
    Also return only absolute value.'''

    n = abs(n)
    if n == 1:
        return [1]
    factor = []
    i = 2 # FIXME loop through prime numbers instead.
    while n > 1:
        while not n % i:
            factor.append(i)
            n /= i
        i += 1
    return factor

def divisors(n):
    '''divisors(number) -> list

    Positive divisors of the number, e.g. divisors(15) -> [1, 3, 5, 15]'''

    if not n:
        return []
    factor = factorized(abs(n))
    unique = set(factor)
    group = ({p**i for i in range(factor.count(p)+1)} for p in unique)
    return sorted(prod(c) for c in cartesian_product(*group))

def summation(n, p=1):
    '''summation(stop_number[, power]) -> int

    Summation of numbers in [1..n], e.g. summation(10) -> 55

    Step of each seq is 1. If you need the summation of odd or even,
    Do some mathematical proove that gives, for example,

        summation(n if n is even) =  2 + 4 + 6 + ... + n
                                  = (1 + 2 + 3 + ... + n/2)*2
                                  = 2 * summation(n/2)

    The start number is also 1. You may now figure out that,

        summation([5..10]) = summation(10) - summation(5-1)

    Avalable power now implement only for p=[0..3]. TODO

    Complexity is O(p log p), (considered power done in O(log p) time).
    While sum(i**p for i in range(1, n+1)) required O(n log p) time.

    see also: <http://en.wikipedia.org/wiki/Bernoulli_number>'''

    if p == 0:
        return n
    elif p == 1:
        return n * (n + 1) // 2
    elif p == 2:
        return n * (n + 1) * (2*n + 1) // 6
    elif p == 3:
        return (n * (n + 1) // 2) ** 2
    else:
        raise NotImplementedError

