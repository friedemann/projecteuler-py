
import primes


def solve():

    tri = 1
    nat = 2
    divs = []
    divcount = 0

    max_divs = 0

    while divcount < 500:

        '''takes years'''
        #divs = primes.get_factors(tri)        
        '''much faster'''
        divcount = primes.get_triangular_factor_count(tri)

        #divcount = len(divs)
        if divcount > max_divs:
            max_divs = divcount
            print(tri, '-', divcount)
            #print(tri, '-', divcount, divs)

        tri = tri + nat
        nat += 1

#solve()

import petools
petools.time('solve', '', 3)
