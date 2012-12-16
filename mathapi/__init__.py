from fractions import Fraction, Decimal
from itertools import product as cartesian_product

class Fraction(Fraction):
    def decimal(self, sep='()'):
        '''Show repeating decimal representation of the fraction.

        >>> Fraction(1, 7).decimal()
        '0.(142857)'

        Warning! Since the repeating part can contain as much digits as
        the size of the denominator (especially if its a prime number),
        this computation might take very long time too.'''

        n, d = self.numerator, self.denominator

        t, s = '', {}
        while n:
            t += str(n // d) + ('.' if not t else '')
            n = 10 * (n % d)
            if n in s:
                break
            s[n] = len(s)
        else:
            return t if t[-1] != '.' else t[:-1]

        r = s[n] - len(s)
        ti, tr = t[:r], t[r:]
        if not sep:
            sep_l, sep_r = '', '...'
            tr *= 2
        elif len(sep) == 1:
            sep_l = sep_r = sep * 3
        else:
            sep_l, sep_r = sep[0], sep[1]

        return ti + sep_l + tr + sep_r


def infinitelist(value):
    '''As function decorator, with initial value.

    Sample usage:

    >>> @infinitelist([1, 2, 3])
    ... def sequence(class_base):
    ...     def __getitem__(self, value):
    ...         # define custom __getitem__ method here.
    ...         super(class_base, self).__getitem__(value)
    ...     return locals()
    ...
    >>> sequence
    [1, 2, 3, ...]
    '''
    def initialize(func):
        class InfiniteList(list):
            __doc__ = func.__doc__

            def under(self, s):
                n = 0
                while self[n] < s:
                    yield self[n]
                    n += 1

            def __iter__(self):
                n = 0
                while True:
                    yield self[n]
                    n += 1
            
            def __repr__(self):
                return super(InfiniteList, self).__repr__()[:-1] + ', ...]'

        # overwrite attributes that are specificaly defined.
        for name, attr in func(InfiniteList).items():
            setattr(InfiniteList, name, attr)

        return InfiniteList(value)
    return initialize


@infinitelist([1, 1])
def fibonacci(base):
    '''Fibonacci sequence'''

    def position(self, n, m={0:1, 1:1}):
        '''An implementation of E.W.Dijkstra method, O(log n).

        see also: <http://www.cs.utexas.edu/users/EWD/ewd06xx/EWD654.PDF>'''
        if n in m:
            return m[n]
        if n % 2:
            m[n] = self.position(n//2, m)**2 + \
                   self.position(n//2, m) * self.position(n//2-1, m) * 2
        else:
            m[n] = self.position(n//2-1, m)**2 + \
                   self.position(n//2, m)**2
        return m[n]

    def __getitem__(self, n):
        while True:
            try:
                return super(base, self).__getitem__(n)
            except IndexError:
                self.append( super(base, self).__getitem__(-1) +
                             super(base, self).__getitem__(-2) )

    return locals()


@infinitelist([2, 3])
def prime(base):
    '''Prime number sequence'''

    def index(self, n):
        if n not in self:
            raise ValueError('{} is not prime'.format(n))
        while n > self[-1]:
            self[len(self)]
        return super(base, self).index(n)

    def __contains__(self, n):
        if not isinstance(n, int):
            raise TypeError
        if n <= 1:
            return False
        for i in self:
            if i**2 > n:
                return True
            if not n % i:
                return False

    def __getitem__(self, n):
        while True:
            try:
                return super(base, self).__getitem__(n)
            except IndexError:
                head = self[self.__sieve_index]**2 + 1
                self.__sieve_index += 1
                last = self[self.__sieve_index]**2
                sieve = list(range(head, last))
                for p in self[:self.__sieve_index]:
                    size = (last - head + (head % -p)) // p + 1
                    sieve[-head % p::p] = [0] * size
                self.extend(p for p in sieve if p)

    def __init__(self, value):
        self.__sieve_index = 0
        super(base, self).__init__(value)

    return locals()


def duality(value):
    '''As function decorator, with initial value.

    Sample usage:

    >>> @duality(1.23456789)
    ... def geek(n):
    ...     return 1/n**2 + 1/n
    ...
    >>> geek * 5
    6.17283945
    >>> geek(9)
    0.12345679012345678
    '''
    def initialize(func):
        class Duality(type(value)):
            __doc__ = func.__doc__

            def __call__(self, *args, **kwargs):
                return func(*args, **kwargs)

        return Duality(value)
    return initialize


@duality((1 + 5**0.5) / 2)
def phi(n):
    '''Duality number-function data type.

    as number: phi -> 1.618033988...
        Golden Ratio, real number where phi == 1 + 1/phi.

    as function: phi(number) -> number
        Euler's totient, number of all 0 < a < n where gcd(a, n) == 1.'''

    if n == 1:
        return 1
    factor = factorized(n)
    group = ((p, factor.count(p)) for p in set(factor))
    return prod((p-1) * p**(k-1) for p, k in group)


@duality(3.141592653589793)
def pi(n):
    '''Duality number-function data type.

    as number: pi -> 3.141592653...
        Ratio of a circle's circumference to its diameter.

    as function: pi(number) -> number
        Prime-counting, number of all 0 < p <= n where p is a prime number'''

    return sum(1 for p in prime.under(n+1))


def prod(l):
    '''prod(iterable) -> value'''

    s = 1
    for n in l:
        s *= n
    return s

def factorized(n):
    '''factorized(number) -> list

    Prime fatorization of the number, e.g. factorized(42) -> [2, 3, 7]
    Returns empty list if 'n' is 0, or [1] if 'n' is 1 (by defination).
    Also return only absolute value.'''

    n = abs(n)
    if n == 1:
        return [1]
    factor = []
    for i in prime:
        if i**2 > n:
            break
        while not n % i:
            factor.append(i)
            n //= i
    if n > 1:
        factor.append(n)
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

