
import itertools

file = open('euler011.txt')
str = ''.join([line.lstrip() for line in file])
file.close()


GRIDSIZE = 20


def grouper(n, iterable, fillvalue = None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue = fillvalue)


def idx(xy):
    return xy[0] + xy[1] * GRIDSIZE


def solve():

    prod = 1
    largest = 0

    num_list = [int(i[0] + i[1] + i[2]) for i in grouper(3, str, ' ')]

    #horizontal
    for y in range(0, 20):
        for x in range(0, GRIDSIZE - 3):
            prod = 1
            for t in (x, y), (x + 1, y), (x + 2, y), (x + 3, y):
                prod = prod * num_list[idx(t)]
            #print(prod, largest)
            largest = prod if prod > largest else largest


    #vertical
    for y in range(0, GRIDSIZE - 3):
        for x in range(0, 20):
            prod = 1
            for t in (x, y), (x, y + 1), (x , y + 2), (x , y + 3):
                prod = prod * num_list[idx(t)]
            largest = prod if prod > largest else largest
    prod = 1

    #diagonal
    for y in range(0, GRIDSIZE - 3):
        for x in range(0, GRIDSIZE - 3):
            prod = 1
            for t in (x, y), (x + 1, y + 1), (x + 2 , y + 2), (x + 3 , y + 3):
                prod = prod * num_list[idx(t)]
            largest = prod if prod > largest else largest

    #reverse diagonal
    for y in range(0, GRIDSIZE - 3):
        for x in range(3, 20):
            prod = 1
            for t in (x, y), (x - 1, y + 1), (x - 2 , y + 2), (x - 3 , y + 3):
                prod = prod * num_list[idx(t)]
            largest = prod if prod > largest else largest


    print(largest)

#solve()

import petools
petools.time('solve', '', 5)
