from math import factorial as f


def newton(n):
    C = lambda n, k: round(f(n) / (f(k) * f(n - k)))
    for i in range(n + 1):
        yield ' '.join(str(C(i, j)) for j in range(i + 1))


while True:
    n = input('Plese enter an number ')
    if n.isdigit():
        n = int(n)
        break
    print('Number must be a non negative integer')

for i in newton(n):
    print(i)
