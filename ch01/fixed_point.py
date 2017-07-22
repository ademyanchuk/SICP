#! /usr/local/bin/python3
TOLERANCE = 0.0000001
dx = TOLERANCE

def fixed_point(f, first_guess):

    def close_enough(v1, v2):
        return abs(v1-v2) < TOLERANCE

    def tryy(guess):
        nxt = f(guess)
        if close_enough(guess, nxt):
            return nxt
        else:
            return tryy(nxt)

    return tryy(first_guess)

def sqrt(x):
    return fixed_point(average_dump(lambda y: x/y), 1.0)

def average_dump(f):
    return lambda x: (x + f(x))/2

# derivate via limit
def deriv (g):
    return lambda x: (g(x + dx) - g(x))/ dx

def cube(x):
    return x*x*x

