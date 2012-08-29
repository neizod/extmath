def sigma(n, power=1):
    '''sigma(n[, power]) -> int

    Summation of numbers in [1, 2, 3, ..., n].
    see more: <http://en.wikipedia.org/wiki/Bernoulli_number>'''
    if power == 0:
        return n
    elif power == 1:
        return n * (n + 1) // 2
    elif power == 2:
        return n * (n + 1) * (2*n + 1) // 6
    elif power == 3:
        return (n * (n + 1) // 2) ** 2
    else:
        raise NotImplementedError

