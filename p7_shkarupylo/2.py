def hexadecimal(a):
    a = int(a)
    hexa = [i for i in range(9)]
    hexa += 'A', 'B', 'C', 'D', 'E', 'F'
    c = str(hexa[a // 16])
    c += str(hexa[a % 16])
    return c


def according(a):
    mistake = 'The number must math to the interval [0;255]'
    if a.isdigit():
        if 0 <= int(a) <= 255:
            return True
    print(mistake)
    return False


hexa_number = ''
entering = 'Enter the {} number which math to the interval [0;255]'
for i in ('first', 'second', 'third'):
    while True:
        a = input(entering.format(i))
        if according(a):
            hexa_number += hexadecimal(a).zfill(2)
            break
print(hexa_number)
