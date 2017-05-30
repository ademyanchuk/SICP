def sqrt(x):

    def sqrt_iter(guess):
        if good_enough(guess):
            return guess
        return sqrt_iter(improve(guess))

    def improve(guess):
        return average(guess, (x / guess))

    def good_enough(guess):
        return abs(guess**2 - x) < 0.001

    return sqrt_iter(1.0)


def average(x, y):
    return (x + y) / 2
