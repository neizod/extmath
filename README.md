Digging into <http://projecteuler.com>, I discover many interesting
mathematical technique, which is not yet

    sigma(n, pow=1) -> value
    - work pretty much like sum(i for i in range(n+1)).
    - but done in O(1) time.
    - always start from 0. so if you need something like:
        sigma(... i=5 to 10) you need to write sigma(10) - sigma(5).
    - (now) support only step=1 and pow=0..3.
    - see more: <http://en.wikipedia.org/wiki/Bernoulli_number>

