import math

def is_prime(p):
    if p < 2:
        return 0
    d = 2
    while d * d <= p:
        if p % d == 0:
            return 0
        d += 1
    return 1


def next_prime(p):
    p += 1
    if is_prime(p):
        return p
    else:
        return next_prime(p)


def solve():
    n = 600851475143
    d = 2
    largest = 2

    while d < math.sqrt(n):
        if n % d == 0:
            largest = d
            print("so far", largest)
        d = next_prime(d)

    print(largest)

solve()

import petools
petools.time('solve', '', 5)


