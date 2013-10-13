
import primes


def solve():

    kgv = 1
    pf = {}

    for i in range(2, 20):
        pf2 = primes.get_prime_factors(i)

        for j in pf2:
            exp = pf2.count(j)

            if j in pf:
                if exp > pf[j]:
                    pf[j] = exp;
            else:
                pf[j] = exp;

    for f, e in pf.items():
        kgv = kgv * f ** e

    print(kgv)

solve()

import petools
petools.time('solve', '', 5)
