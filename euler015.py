
import itertools
import math

GRIDSIZE = 20


def solve2():

    # we're talking about the central binomial coefficient here... :/
    #
    #  2n!
    # ------
    #  n!^2

    fac = math.factorial
    cbc = fac(2 * GRIDSIZE) / pow(fac(GRIDSIZE), 2)
    print(cbc)

def solve():
    # ---
    # bf: complexity way too bad
    # GS>5 not solvable in reasonable time
    # ---

    steps = 'x' * GRIDSIZE + 'y' * GRIDSIZE
    print(steps)

    perms = itertools.permutations(steps)

    cache = []

    for p in perms:
        if p not in cache:
            cache.append(p)
            #print(p)

    print(len(cache))

#solve2()

import petools
petools.time('solve2', '', 5)
