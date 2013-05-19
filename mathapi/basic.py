def sqrt(n):
    '''sqrt(non_negative_integer) -> integer

    Return integer square root of an input number '''

    if n == 0: 
        return 0 
    x = 2 ** sum(divmod(n.bit_length(), 2))
    while True: 
        y = x + n // x 
        y //= 2 
        if y >= x: 
            return x 
        x = y


def product(l, s=1):
    '''product(iterable[, int]) -> value
    
    Return production of numbers, eager eval (no short circit when face 0).
    This function may have initial value as second argument.'''

    for n in l:
        s *= n
    return s


def group(l):
    '''group(iterable) -> set of tuple of key-value'''

    d = {}
    for k in l:
        d[k] = d.get(k, 0) + 1
    return d.items()


def sumexp(r, k):
    '''sumexp(base, stop_power) -> int

    Summation from r**0 to r**k, by telescoping method.'''

    if r == 1:
        return k + 1
    return (r**(k+1) - 1) // (r - 1)


def sumpow(n, p=1):
    '''sumpow(stop_number[, power]) -> int

    Summation from 1**p to n**p, calculate by Bernulli/Faulgaber's formula.

    >>> sumpow(10)
    55
    >>> sumpow(10, 2)
    385

    Step of each seq is 1. If you need the summation of odd or even,
    Do some mathematical proove that gives, for example,

        summation(n if n is even) =      2 + 4 + 6 + ... + n
                                  = 2 * (1 + 2 + 3 + ... + n/2)
                                  = 2 * summation(n/2)

    The start number is also 1. You may now figure out that,

        summation([5..10]) = summation(10) - summation(5-1)

    Avalable power now implement only for p=[0..4]. TODO

    Complexity is O(p log p), (considered power done in O(log p) time).
    While sum(i**p for i in range(1, n+1)) required O(n log p) time.

    see also: <http://en.wikipedia.org/wiki/Bernoulli_number>'''

    if p == 0:
        return n
    elif p == 1:
        # triangular numbers
        return n * (n + 1) // 2
    elif p == 2:
        # square pyramidal numbers
        return n * (n + 1) * (2*n + 1) // 6
    elif p == 3:
        # square triangular numbers
        return (n * (n + 1) // 2) ** 2
    elif p == 4:
        return (6*n**5 + 15*n**4 + 10*n**3 - n) // 30
    else:
        raise NotImplementedError
