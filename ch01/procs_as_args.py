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
# Example of using high abstraction to create sum_cubes again

def cube(x):
    return x**3

def inc(n):
    return n+1

def sum_cubes_high(a, b):
    return summ(cube, a, inc, b)

# Another example of using high abstraction

def pi_sum_high(a,b):
    def pi_term(x):
        return 1/(x*(x+2))
    def pi_next(x):
        return x+4

    return summ(pi_term, a, pi_next, b)
