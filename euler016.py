
import functools


def solve():

    n = str(pow(2, 1000))
    s = functools.reduce(lambda x, y: x + y, [int(i) for i in n])
    print(s)

solve()

#import petools
#petools.time('solve2', '', 5)
