#! /usr/local/bin/python3
TOLERANCE = 0.00001

def fixed_point(f, first_guess):

    def close_enough(v1, v2):
        return abs(v1-v2) < TOLERANCE

    def tryy(guess):
        nxt = f(guess)
        print("Приближение: {}".format(nxt))
        if close_enough(guess, nxt):
            return nxt
        else:
            return tryy(nxt)

    return tryy(first_guess)

def sqrt(x):
    return fixed_point(lambda y: (y + x/y)/2, 1.0)

def average_dump(f):
    return lambda x: (x + f(x))/2