

def solve():

    s_sq = sum([i * i for i in range(1, 101)])
    s = sum(i for i in range(1, 101))
    sq_s = s * s

    print(sq_s - s_sq)

solve()

import petools
petools.time('solve', '', 5)
