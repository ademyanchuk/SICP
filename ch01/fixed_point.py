#! /usr/local/bin/python3
TOLERANCE = 0.00001

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