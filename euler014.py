
#import sys
#sys.setrecursionlimit(5000)

def sequence(n, s):

    if s == None:
        s = []

    s.append(n)

    if n == 1:
        return s
    elif n % 2 == 0:
        n1 = n // 2
    else:
        n1 = 3 * n + 1

    return sequence(n1, s)


def get_seq_length():
    '''speed up: cache known starting id lengths'''
    #TBI
    pass


def solve():
    longest = 0
    n = 0
    for i in range(1, 1000000):
        l = len(sequence(i, None))
        if l > longest:
            longest = l
            n = i
    print(n, longest)


def solve2():

    longest = 0
    n = 0
    for i in range(1, 1000000):
        l = get_seq_length(i)
        if l > longest:
            longest = l
            n = i
    print(n, longest)

solve()
