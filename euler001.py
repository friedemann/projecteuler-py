


def solve():
    s = 0
    for i in range(1000):
        if i % 5 == 0 or i % 3 == 0:
            s += i
    print(s)

solve()

import petools
petools.time('solve', '', 5)
