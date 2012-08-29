def factorized(n):
    '''factorized(n) -> list

    Prime fatorization of the number, e.g. factorized(42) -> [2, 3, 7]
    Returns empty list if 'n' is 0, 1. Also return only absolute value.'''

    factor = []
    n = abs(n)
    i = 2 # FIXME loop through prime numbers instead.
    while n > 1:
        while not n % i:
            factor.append(i)
            n /= i
        i += 1
    return factor

def sigma(n, p=1):
    '''sigma(number[, power]) -> int

    Summation of numbers in [1..n], e.g. sigma(10) -> 55
    Complexity is O(p), (while sum(range(1, n+1)) does in O(n) time).
    Avalable power now implement only for p=[0..3].

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

