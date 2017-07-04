#! /usr/local/bin/python3
import time

def  smallest_divisor(n):
    return find_divisor(n, 2)

def next_divisor(test_divisor):
    if test_divisor == 2:
        return 3
    else:
        return test_divisor + 2

def find_divisor(n, test_divisor):
    while (test_divisor**2 > n ==False or divides(test_divisor, n) == False):
        test_divisor = next_divisor(test_divisor)

    if test_divisor**2 > n:
        return n
    else:
        return test_divisor

def divides(a,b):
    return b%a == 0

def isPrime(n):
    return smallest_divisor(n) == n

def search_primes(start, stop):
    count = 0
    for n in range(start, stop):
        if count == 3:
            break
        if isPrime(n) and n%2 != 0:
            print(n)
            count+=1
    return None

####
# Measurements
###
# %timeit(isPrime(1009)) ---- 344 µs ± 5.66 µs per loop
# %timeit(isPrime(10007)) ---- 3.59 ms ± 48.2 µs per loop
# %timeit(isPrime(100003)) ---- 35.9 ms ± 775 µs per loop
# %timeit(isPrime(1000003)) ---- 346 ms ± 3.52 ms per loop