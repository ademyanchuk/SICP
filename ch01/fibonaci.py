#! /usr/local/bin/python3
# example of tree recursion
import logging

# uncomment below for disable logging
logging.disable(logging.CRITICAL)

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start program')

def fib(n):
    logging.debug('Start fibonacci ({})'.format(n))
    if n == 0:
        logging.debug("Base case 0")
        return 0
    elif n == 1:
        logging.debug("Base case 1")
        return 1
    else:
        logging.debug('recursion tree to {} - 1 and {} - 2'.format(n, n))
        return fib(n-1) + fib(n-2)

# print(fib(5))


# example of iterative process
def fib_v1(n):
    logging.debug('Start fib version_1 ({})'.format(n))
    return fib_iter_v1(1, 0, n)

def fib_iter(a, b, count):
    if count == 0:
        logging.debug("Base case 0")
        return b
    else:
        logging.debug('Iterating with a = {}, b = {} and count = {}'.format(a,b,count))
        return fib_iter(a+b, a, count-1)


# fib_iter using while loop
def fib_iter_v1(a,b,count):
    if count == 0:
        return 0
    while count > 0:
        temp = a
        a = a + b
        b = temp
        count -= 1
    return b

# print(fib_v1(5))
logging.debug("End of debugging")

# timeit for recursive function fib_iter
# %timeit fibonaci.fib_v1(10)
# 19.4 µs ± 340 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
# %timeit fibonaci.fib_v1(100)
# 177 µs ± 611 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

# timeit for iterative function fib_iter
# %timeit fibonaci.fib_v1(10)
# 2.48 µs ± 37.2 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
# %timeit fibonaci.fib_v1(100)
# 11.6 µs ± 190 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

# Both have iterative process inside, but Python think
# first case is really recursion.