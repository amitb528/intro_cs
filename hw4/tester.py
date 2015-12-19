import time
import random


def test(func, args=None, times=1):
    t = time.clock()
    for i in range(0, times):
        func(*args)
    return (time.clock() - t) / times


def test_max(func, n, times):
    t = time.clock()
    for i in range(0, times):
        l = [random.randint(0, 10000) for i in range(0, n)]
        func(l)
    return (time.clock() - t) / times