import math

try:
    print('Now enter please coefficients of our quadratic equation')
    a = float(input('a (the highest term coefficient) '))
    b = float(input('b (the coefficient at x) '))
    c = float(input('c (free member) '))
    D = math.sqrt(b ** 2 - 4 * a * c)
    x_1 = (-b + D) / (2 * a)
    x_2 = (-b - D) / (2 * a)
    print('The first solution {}, the second {}'.format(round(x_1, 2), round(x_2, 2)))
except Exception as ex:
    print(ex)
