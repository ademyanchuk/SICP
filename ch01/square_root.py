def sqrt(x):
    return sqrt_iter(1.0, x)


def sqrt_iter(guess, x):
    if good_enough(guess, x):
        return guess
    return sqrt_iter(improve(guess, x), x)

def improve(guess, x):
    return average(guess, (x / guess))

def average(x, y):
    return (x + y) / 2

def good_enough(guess, x):
    return abs(guess**2 - x) < 0.001


