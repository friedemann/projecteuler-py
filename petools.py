from timeit import Timer

def time(fn, arg, rpt=5):
    t = Timer(fn + "(" + arg + ")", "from __main__ import " + fn)
    print("%.5f ms/pass" % (1000 / rpt * t.timeit(number=rpt)))
