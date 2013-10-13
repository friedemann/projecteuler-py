
def solve():

    found = False

    for a in range(0, 1000):
        b = 1000
        while a < b:
            c = 1000 - a - b

            if b < c:
                if a * a + b * b == c * c:
                    print(a, b, c, a * b * c)
                    found = True
            b -= 1
            if found: break
        if found: break

#solve()

import petools
petools.time('solve', '', 5)
