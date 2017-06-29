#! /usr/local/bin/python3
import time

def  smallest_divisor(n):
    return find_divisor(n, 2)

def find_divisor(n, test_divisor):
    if test_divisor**2 > n:
        return n
    elif divides(test_divisor, n):
        return test_divisor
    else:
        return find_divisor(n, test_divisor + 1)

def divides(a,b):
    return b%a == 0

def isPrime(n):
    return smallest_divisor(n) == n

def timedPrimeTest(n):
    print("\n")
    print(n)
    return startPrimeTest(n, round(time.time() * 1000000))

def startPrimeTest(n, start_time):
    if isPrime(n):
        return reportPrime(round(time.time() * 1000000) - start_time)

def reportPrime(elapsed_time):
    print(" *** ")
    print(elapsed_time)