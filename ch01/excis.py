def sum_squares(a,b,c):
    if a <= b <= c:
        return b**2 + c**2
    elif b <= c <= a:
        return c**2 + a**2
    else:
        return b**2 + a**2

print(sum_squares(-1, -2, -3))