#! /usr/local/bin/python3

def square(x):
    return x*x

# tree recursion
def f(n):
    if n < 3:
        return n
    else:
        return f(n-1)+f(n-2)+f(n-3)


# same function with iterative process
def f_v1(n):
    return iter_f(2,1,0,n)


def iter_f(a,b,c,count):
    if count < 3:
        return count
    while count >= 3:
        result = a + b + c
        c = b
        b = a
        a = result
        count -= 1
    return result

def pascal(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1,1]
    else:
        result = [1]
        result.extend([pascal(n-1)[i]+pascal(n-1)[i+1] for i in range(len(pascal(n-1))) if i < len(pascal(n-1))-1])
        result.append(1)
        return result

def gen_pascal():
    n = 0
    result = []
    while True:
        if n == 0:
            result.append([1])
        elif n == 1:
            result.append([1,1])
        else:
            temp = [1]
            temp.extend([result[n-1][i]+result[n-1][i+1] for i in range(len(result[n-1])) if i < len(result[n-1])-1])
            temp.append(1)
            result.append(temp)
        yield result[n]
        n += 1

def pascal_v1(n):

    gen = gen_pascal()
    result = next(gen)
    for i in range(n):
        result = next(gen)
    return result

def expt(b,n):
    if n == 0:
        return 1
    else:
        return b * expt(b, n-1)

def expt_v1(b,n):
    return expt_iter(b,n,1)

def expt_iter(b,counter,product):
    while counter > 0:
        product *= b
        counter -= 1
    return product

def fast_expt(b,n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(fast_expt(b, n//2))
    else:
        return b * fast_expt(b, n - 1)

# iterative process log(n) time
def fast_expt_iter(b,n):
    if b == 1 or b == 0:
        return b
    a = 1
    while n > 0:
        if n % 2 == 0:
            b = b*b
            n = n//2
        else:
            a = a * b
            n = n - 1
    return a
