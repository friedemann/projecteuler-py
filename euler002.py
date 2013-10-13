

def solve():
    s = 0
    a, b = 0, 1
    while b < 4000000:
        if b % 2 == 0:
            s += b
        a, b = b, a + b
    print(s)


solve()

import petools
petools.time('solve', '', 5)
