#! /usr/local/bin/python3

def average(a,b):
    return (a+b)/2

def close_enough(a,b):
    return abs(a-b) < 0.001

def search_iter(f, neg_point, pos_point):
    midpoint = average(neg_point, pos_point)
    while not close_enough(neg_point, pos_point):
        test_value = f(midpoint)
        if test_value > 0:
            pos_point = midpoint
        elif test_value < 0:
            neg_point = midpoint
        else:
            break
        midpoint = average(neg_point, pos_point)
    return midpoint

def search_recursive(f, neg_point, pos_point):
    midpoint = average(neg_point, pos_point)
    if close_enough(neg_point, pos_point):
        return midpoint
    else:
        test_value = f(midpoint)
        if test_value > 0:
            return search_recursive(f, neg_point, midpoint)
        elif test_value < 0:
            return search_recursive(f, midpoint, pos_point)
        else:
            return midpoint

def half_interval_method(f, a, b):
    a_value = f(a)
    b_value = f(b)
    if a_value < 0 and b_value > 0:
        return search_recursive(f, a, b)
    elif b_value < 0 and a_value > 0:
        return search_recursive(f, b, a)
    else:
        return (print("У аргументов {} {} не разные знаки".format(a,b)))