#! /usr/local/bin/python3

def sum_integers(a,b):
    if a > b:
        return 0
    else:
        return a + sum_integers(a+1,b)

def sum_cubes(a, b):
    if a > b:
        return 0
    else:
        return a**3 + sum_cubes(a+1, b)

# more abstract procedure
def summ(term, a, nxt, b):
    if a>b:
        return 0
    else:
        return term(a) + summ(term, nxt(a), nxt, b)

# Same  procedure, but iterative.
def sum_iter(term, a, nxt, b):
    result = 0
    while a <= b:
        result += term(a)
        a = nxt(a)
    return result

# Abstract product procedure
def product(term, a, nxt, b):
    if a > b:
        result = 0
    else:
        result = term(a)
    while a < b:
        a = nxt(a)
        result *= term(a)
    return result

# Higher abstraction - accumulation
def accumulate(combiner, null_value, term, a, nxt, b):
    if a > b:
        result = null_value
    else:
        result = term(a)
    while a < b:
        a = nxt(a)
        result = combiner(result, term(a))
        print(result)
    return result

def sum_from_accum(term, a, nxt, b):
    return accumulate(add, 0, term, a, nxt, b)

# Example of using high abstraction to create sum_cubes again

def cube(x):
    return x**3

def inc(n):
    return n+1

def ident(a):
    return a

def mult(a, b):
    return a*b

def add(a ,b):
    return a + b

def sum_cubes_high(a, b):
    return sum_iter(cube, a, inc, b)

# Another example of using high abstraction

def pi_sum_high(a,b):
    def pi_term(x):
        return 1/(x*(x+2))
    def pi_next(x):
        return x+4

    return summ(pi_term, a, pi_next, b)

# Factorial using product
def factorial(x):
    if x == 0:
        return 1
    else:
        return product(ident, 1, inc, x)
