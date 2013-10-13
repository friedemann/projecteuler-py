
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


def get_prime_factors(n, amt = 99, mult = True):

    p = 2
    pf = list()
    rmd = 0

    while p <= math.sqrt(n) and len(pf) < amt:
        rmd = n % p
        if  rmd == 0:
            if mult:
                pf.append(p)
            elif not mult and pf.count(p) == 0:
                pf.append(p)

            n = n / p

        elif rmd < p:
            p = next_prime(p)

    return pf


def get_factors(n, amt = 999):

    d = 1
    f = list()
    rmd = 0

    while d <= n and len(f) < amt:
        rmd = n % d
        if  rmd == 0:
            f.append(d)

        d += 1

    return f


#why only factor count?

'''              _stop calculating here, you already have all factors (!)
               /
n    28 28 28 |28 28 28    
fac   1  2  4 | 7 14 28
===  ==================
div  28 14  7 | 4  2  1
'''
def get_triangular_factor_count(n):

    d = 1
    f = 0
    rmd = 0

    while d <= n:
        rmd = n % d
        if  rmd == 0:

            x = n / d

            if(x < d):
                return f * 2
            elif(x == d):
                return f * 2 + 1

            f += 1

        d += 1

    return f
