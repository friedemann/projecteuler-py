

def solve():

    ONE_TO_NINE = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']  #36
    THIR_TO_NINE_ = ['thir', 'four', 'fif', 'six', 'seven', 'eigh', 'nine']                 #27
    TWEN_TO_NINE_ = ['twen', 'thir', 'for', 'fif', 'six', 'seven', 'eigh', 'nine']         #31
    TEEN = 'teen'
    TY = 'ty'
    TEN = 'ten'
    ELEVEN = 'eleven'
    TWELVE = 'twelve'
    HUNDRED = 'hundred'
    AND = 'and'
    ONETHOUSAND = 'onethousand'


    #1-19
    s1_19 = [i for i in ONE_TO_NINE]
    s1_19 += [TEN, ELEVEN, TWELVE]
    s1_19 += [i + TEEN for i in THIR_TO_NINE_]

    #20-99
    s20_99 = [i + TY for i in TWEN_TO_NINE_]
    for i in TWEN_TO_NINE_:
        s20_99 += [i + TY + j for j in ONE_TO_NINE]

    s1_99 = s1_19 + s20_99

    #100-999
    s100_999 = [i + HUNDRED for i in ONE_TO_NINE]
    for i in ONE_TO_NINE:
        s100_999 += [i + HUNDRED + AND + j for j in s1_99]

    s1_1000 = s1_99 + s100_999 + [ONETHOUSAND]

    #for i in s1_1000: print(i)
    print(sum(len(i) for i in s1_1000))

#solve()

import petools
petools.time('solve', '', 5)
