
import functools

file = open('euler013.txt')
nums = [int(line.strip()) for line in file]
file.close()


def solve():
    sum = functools.reduce(lambda x, y: x + y, nums)
    print(sum)

#solve()

import petools
petools.time('solve', '', 5)
