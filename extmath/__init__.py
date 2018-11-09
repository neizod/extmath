from fractions import Fraction, Decimal
from extmath.meta import infinitelist, duality, indexargument
from extmath.basic import sqrt, product, group, sumexp, sumpow
from extmath.number_theory import primes, phi, pi, sigma, factorized, divisors


def _decimal(self, sep='()'):
    '''Show repeating decimal representation of the fraction.

    >>> Fraction(1, 7).decimal()
    '0.(142857)'

    Warning! Since the repeating part can contain as much digits as
    the size of the denominator (especially if its a prime number),
    this computation might take very long time too.'''

    n, d = self.numerator, self.denominator
    if n == 0:
        return '0.0'

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

Fraction.decimal = _decimal
del _decimal


class NumeralSystem:
    def int(self, string):
        l = []
        for digit in string:
            if digit not in self.digits:
                raise KeyError('digit not exists in this numeral system.')
            l.append(self.digits.index(digit))
        return sum(v * self.base**k for k, v in enumerate(reversed(l)))

    def str(self, integer):
        l = []
        while integer:
            integer, remaining = divmod(integer, self.base)
            l.append(remaining)
        return ''.join(self.digits[n] for n in reversed(l))

    def __init__(self, digits):
        if not digits:
            raise ValueError('numeral system could not represent with empty.')
        if len(digits) == 1:
            raise ValueError('numeral system should not have single digit.')
        self.digits = digits
        self.base = len(digits)


@infinitelist([1, 1])
def fibonaccis(base):
    '''Fibonacci sequence'''

    def __call__(self, n, m={0: 1, 1: 1}):
        '''An implementation of E.W.Dijkstra method, O(log n).

        see also: <http://www.cs.utexas.edu/users/EWD/ewd06xx/EWD654.PDF>'''

        if n not in m:
            if n % 2:
                m[n] = self(n//2, m)**2 + self(n//2-1, m) * self(n//2, m) * 2
            else:
                m[n] = self(n//2, m)**2 + self(n//2-1, m)**2
        return m[n]

    def __generate__(self):
        self.append( super(base, self).__getitem__(-1) +
                     super(base, self).__getitem__(-2) )

    return locals()
