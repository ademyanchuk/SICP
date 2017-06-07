#! /usr/local/bin/python3
import logging

step = 0

# uncomment below for disable logging
# logging.disable(logging.CRITICAL)

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start program')
def cube(x):
    return x**3

def p(x):
    global step
    logging.debug("Step #: {}".format(step))
    step += 1
    return 3*x - 4*cube(x)

def sine(angle):
    if not abs(angle) > 0.1:
        return angle
    else:
        return p(sine(angle/3.0))

print(sine(12.15))




