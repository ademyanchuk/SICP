def sqrt(x):
    return sqrt_iter(1.0, x)

def qubert(x):
    return qubert_iter(1.0, x)


def sqrt_iter(guess, x):
    if x == 1:
        return x
    prev_guess = guess
    while not good_enough(guess, prev_guess):
        prev_guess = guess
        guess = improve(guess, x)

    return guess

def qubert_iter(guess, x):
    if x == 1:
        return x
    prev_guess = guess
    while not good_enough(guess, prev_guess):
        prev_guess = guess
        guess = improve_qube(guess, x)
    return guess

def improve(guess, x,):
    return average(guess, (x / guess), 2)

def improve_qube(guess, x):
    return average(guess*2, (x / guess**2), 3)

def average(x, y, n):
    return (x + y) / n

def good_enough(guess, prev_guess):
    return abs(1 - (prev_guess / guess)) < 0.001 and abs(1 - (prev_guess / guess)) != 0


