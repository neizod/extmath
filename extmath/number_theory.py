from itertools import product as cartesian_product
from extmath.meta import infinitelist, duality, indexargument
from extmath.basic import product, group, sumexp


@infinitelist([2, 3])
def primes(base):
    '''Prime number sequence'''

    def index(self, n):
        if n not in self:
            raise ValueError('{} is not prime number'.format(n))
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

    def __generate__(self):
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


@duality((1 + 5**0.5) / 2)
def phi(n):
    '''Duality number-function data type.

    as number: phi -> 1.618033988...
        Golden Ratio, real number where phi == 1 + 1/phi.

    as function: phi(number) -> number
        Euler's totient, number of all 0 < a < n where gcd(a, n) == 1.'''

    if n == 1:
        return 1
    return product((p-1) * p**(k-1) for p, k in group(factorized(n)))


@duality(3.141592653589793)
def pi(n):
    '''Duality number-function data type.

    as number: pi -> 3.141592653...
        Ratio of a circle's circumference to its diameter.

    as function: pi(number) -> number
        Prime-counting, number of all 0 < p <= n where p is a prime number'''

    return sum(1 for p in primes.under(n+1))


@indexargument
def sigma(n, x=1):
    '''sigma(int) -> int
    
    Divisor's sigma function'''

    if n == 1:
        return 1
    return product(sumexp(p**x, k) for p, k in group(factorized(n)))


def trial_div(n):
    n = abs(n)
    if n == 1:
        return [1]
    factor = []
    for i in primes:
        if i**2 > n:
            break
        while not n % i:
            factor.append(i)
            n //= i
    if n > 1:
        factor.append(n)
    return factor


def factorized(n):
    '''factorized(number) -> list

    Prime fatorization of the number, e.g. factorized(42) -> [2, 3, 7]
    Return empty list if 'n' is 0, or [1] if 'n' is 1 (by defination).
    Also return only absolute value.'''
    
    return trial_div(n)


def divisors(n):
    '''divisors(number) -> list

    Positive divisors of the number, e.g. divisors(15) -> [1, 3, 5, 15]'''

    if not n:
        return []
    factor_set = ({p**i for i in range(k+1)} for p, k in group(factorized(n)))
    return sorted(product(c) for c in cartesian_product(*factor_set))
