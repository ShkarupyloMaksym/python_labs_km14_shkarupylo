def root2(n):
    return n ** (1 / 2)


def root3(n):
    if n >= 0:
        sign = 1
    else:
        sign = -1
    return sign * (abs(n) ** (1 / 3))
