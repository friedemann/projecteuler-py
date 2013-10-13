

def is_pali(n):

    s_n = str(n)
    ln = len(s_n)

    if ln == 1:
        return 1
    elif s_n[0] == s_n[-1]:
        if ln == 2:
            return 1
        else:
            return is_pali(s_n[1:ln - 1])
    else:
        return 0


def solve():

    largest = 0

    for a in range(999, 0, -1):
        for b in range(999, 0, -1):

            p = a * b
            if is_pali(p) and p > largest:
                largest = p

    print(largest)

solve()

import petools
petools.time('solve', '', 5)
