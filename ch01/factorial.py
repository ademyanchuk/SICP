#! /usr/local/bin/python3

# recursive method for getting factorial with deferred operations
# LINEAR RECURSIVE PROCESS
def factorial(n):
    if n == 1:
        return 1
    else:
     return n * factorial(n-1)

# ITERATIVE PROCESS

def factorial_v1(n):
    return fac_iter(1,1,n)

def fac_iter(product, counter, max_count):
    if counter > max_count:
        return product
    else:
        return fac_iter(counter*product, counter+1, max_count)