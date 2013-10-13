
import primes

def solve():

    sum = 0
    p = 2

    while p < 2000000:
        sum += p
        p = primes.next_prime(p)

    print(p)
    print(sum)

solve()

#import petools
#petools.time('solve', '', 2)
