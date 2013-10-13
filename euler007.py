
import primes

def solve():

    i = 1
    p = 2

    while i < 10001:
        p = primes.next_prime(p)
        i += 1

    print(p)

solve()

import petools
petools.time('solve', '', 5)
