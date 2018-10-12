def infinitelist(value):
    '''As function decorator, with initial value.

    Sample usage:

    >>> @infinitelist([0, 1, 4, 9])
    ... def sequence(class_base):
    ...     def __generate__(self):
    ...         self.append(len(self) ** 2)
    ...     return locals()
    ...
    >>> sequence
    [0, 1, 4, 9, ...]
    >>> sequence[10]
    100
    >>> sequence
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, ...]

    Since __getitem__ can be tricky (accept slice object, lots of boilerplate),
    __generate__ can be use to figure out next-missing items instead.
    It must be a function that accept `self` as one-and-only argument.
    New items can be added by `self.append` or `self.extend`, no returns.
    However, supplying other version of __getitem__ also possible.
    '''
    def initialize(func):
        class InfiniteList(list):
            __doc__ = func.__doc__

            def under(self, s):
                n = 0
                while self[n] < s:
                    yield self[n]
                    n += 1

            def __getitem__(self, value):
                if isinstance(value, slice):
                    if value.start is not None:
                        self[value.start]
                    if value.stop is not None:
                        self[value.stop]
                while True:
                    try:
                        return super(InfiniteList, self).__getitem__(value)
                    except IndexError:
                        self.__generate__()

            def __getslice__(self, start, stop):
                '''python2 backward compatibility'''
                return self[slice(start, stop, None)]

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


def duality(value):
    '''As function decorator, with initial value.

    Sample usage:

    >>> @duality(1.23456789)
    ... def geek(n):
    ...     return 1.0 / n**2 + 1.0 / n
    ...
    >>> geek * 5
    6.17283945
    >>> geek(9)
    0.12345679012345678
    '''
    def initialize(func):
        class Duality(type(value)):
            __doc__ = func.__doc__
            __call__ = func.__call__
        return Duality(value)
    return initialize


def indexargument(func):
    class IndexArgument:
        __doc__ = func.__doc__
        __repr__ = func.__repr__
        __call__ = func.__call__
        def __getitem__(self, x):
            def partial(*args):
                args += (x,)
                return func(*args)
            partial.__name__ = func.__name__ + '[{}]'.format(x)
            return partial
    return IndexArgument()
