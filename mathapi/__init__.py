from fractions import Fraction
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

        t, s = '', []
        while s.count(n) < 2:
            t += str(n // d) + ('.' if not t else '')
            n %= d
            if not n:
                break
            n *= 10
            s.append(n)
        else:
            r = s.index(s.pop()) - len(s)
            ti, tr = t[:r], t[r:]
            if not sep:
                sep_l, sep_r = '', '...'
                tr *= 2
            elif len(sep) == 1:
                sep_l = sep_r = sep * 3
            else:
                sep_l, sep_r = sep[0], sep[1]

            return ti + sep_l + tr + sep_r

        return t if t[-1] != '.' else t[:-1]


class InfinityList(list):
    def under(self, s):
        n = 0
        while self[n] < s:
            yield self[n]
            n += 1
        #return super(InfinityList, self).__iter__()

    def __iter__(self):
        n = 0
        while True:
            yield self[n]
            n += 1
    
    def __str__(self):
        return super(InfinityList, self).__str__()[:-1] + ', ...]'

    def __repr__(self):
        return super(InfinityList, self).__repr__()[:-1] + ', ...]'


class fibonacci(InfinityList):
    def __getitem__(self, n):
        while True:
            try:
                return super(InfinityList, self).__getitem__(n)
            except IndexError:
                self.append( super(InfinityList, self).__getitem__(-1) +
                             super(InfinityList, self).__getitem__(-2) )

    def __init__(self):
        super(InfinityList, self).__init__([1, 1])


class prime(InfinityList):
    def __getitem__(self, n):
        while True:
            try:
                return super(InfinityList, self).__getitem__(n)
            except IndexError:
                c = super(InfinityList, self).__getitem__(-1)
                while True:
                    c += 2
                    for p in self.under(int(c**(1.0/2.0)) + 1):
                        if not c % p:
                            break
                    else:
                        self.append(c)
                        break

    def __init__(self):
        super(InfinityList, self).__init__([2, 3])


fibonacci = fibonacci()
prime = prime()


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
        while not n % i:
            factor.append(i)
            n /= i
        if n == 1:
            break
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

