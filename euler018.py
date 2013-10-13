
import numpy
np = numpy
np.set_printoptions(linewidth = 120)

tri_str = ''
f = open("euler067.txt", "r").readlines()
for l in f:
    tri_str += l

TRISIZE = 100

def solve():

    mx = np.zeros((TRISIZE, TRISIZE), numpy.int)

    #read in
    x, y = 0, 0
    for i in tri_str.replace('\n', ' ').split(' '):
        mx[x][y] = int(i)
        if x == 0: x, y = y + 1, x
        else: x, y = x - 1, y + 1

    #add up larger node values bottom to top
    x, y = TRISIZE - 2, 0
    while x + y >= 0:
        mx[x][y] += max(mx[x + 1][y], mx[x][y + 1])

        if x == 0: x, y = y - 1, x
        else: x, y = x - 1, y + 1

    print(mx[0][0])

#solve()

import petools
petools.time('solve', '', 5)
