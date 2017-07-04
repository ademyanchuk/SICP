#! /usr/local/bin/python3

from random import randint

def isEven(integer):
    return integer%2 == 0

# return reminder of base^exp after dividing by m
# i.e (2**5)%5 = 2
def expmod(base, exp, m):
    if exp == 0:
        return 1
    elif isEven(exp):
        return (expmod(base, exp/2, m) ** 2)%m
    else:
        return (base*(expmod(base, exp-1, m)))%m

def fermatTest(n):
    def tryIt(a):
        # return (a**n)%n == a -- this method is really slow
        return expmod(a, n, n) == a  # this one is log(n)
    return tryIt(randint(1, n-1))

def isPrime_fast(n, times):
    if times == 0:
        return True
    elif fermatTest(n):
        return isPrime_fast(n, times-1)
    else:
        return False

####
# Measurements
###
# %timeit(isPrime_fast(1009, 10)) -- 113 µs ± 340 ns per loop
# %timeit(isPrime_fast(10007, 10)) -- 148 µs ± 1.79 µs per loop
# %timeit(isPrime_fast(100003, 10)) -- 177 µs ± 2.41 µs per loop
# %timeit(isPrime_fast(1000003, 10)) -- 205 µs ± 4.5 µs per loop
