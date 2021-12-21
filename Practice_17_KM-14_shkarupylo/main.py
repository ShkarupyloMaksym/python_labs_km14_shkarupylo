from exp_root.exponitation import exp2, exp3
from exp_root.root import root2, root3
from factorial.factorial import fact
from logarithm.logarithm import log, lg, ln


def check(a, typee):
    try:
        typee(a)
        return True
    except:
        return False


def numbers_split_or(item_list, word='or'):
    item_list_new = [str(i + 1) for i in range(len(item_list))]
    numbers = item_list_new[0]
    if len(item_list_new) == 1:
        return numbers
    for i in item_list_new[1:-1]:
        numbers += ', ' + i
    if len(item_list) > 1:
        numbers += f" {word} " + item_list_new[-1]
    return numbers


def input_from_numbers(item_list):
    for i, j in enumerate(item_list):
        print(f'{i + 1}) {j}')
    num = numbers_split_or(item_list)
    while True:
        n = input('Choose {} '.format(num))
        if n in [str(i + 1) for i in range(len(item_list))]:
            print('_' * 20)
            return n
        print('Error in the input')


def main():
    exp = [exp2, exp3]
    exp_str = ['exp2', 'exp3']
    root = [root3, root2]
    root_str = ['cubic root', 'square root']
    exponential_or_root_str = ['exp', 'root']
    logarithm = [log, lg, ln]
    logarithm_str = ['log', 'lg', 'ln']
    functions_str = ['factorial', 'logarithm', 'exponential_or_root']

    n = input_from_numbers(functions_str)

    if n == '1':
        print('You have chosen factorial function')
        while True:
            n = input('Enter the natural number:')
            if n.isdigit() and n != '0':
                break
            print('Error in the input')
        print('Factorial of {} is {}'.format(n, fact(int(n))))
        return fact(int(n))
    elif n == '2':
        print('You have chose logarithm function')

        n = input_from_numbers(logarithm_str)
        if n == '1':
            print('You have chosen the log:')
            while True:
                a = input('Please enter the base of the logarithm')
                if check(a, float) and a[0] != '-' and a != '0' and a != '1':
                    a = float(a)
                    break
                print('Error in the input')
            while True:
                b = input('Please enter number')
                if check(b, float) and b[0] != '-' and b != '0':
                    b = float(b)
                    break
                print('Error in the input')
            b = [a, b]
        elif n == '2':
            print('You have chosen the lg:')
            while True:
                b = input('Please enter number')
                if check(b, float) and b[0] != '-' and b != '0':
                    b = float(b)
                    break
                print('Error in the input')
            b = [b]
        elif n == '3':
            print('You have chosen the ln:')
            while True:
                b = input('Please enter number')
                if check(b, float) and b[0] != '-' and b != '0':
                    b = float(b)
                    break
                print('Error in the input')
            b = [b]
        print('Logarithm of {num} = {func}'.format(num=str(b)[1:-1], func=logarithm[int(n) - 1](*b)))
        return logarithm[int(n) - 1](*b)
    elif n == '3':
        print('You have chosen exp_root function')
        n = input_from_numbers(exponential_or_root_str)
        if n == '1':
            n = input_from_numbers(exp_str)
            if n == '1':
                print('You have chosen exp in 2')
                while True:
                    a = input('Please enter number')
                    if check(a, float):
                        break
                    print('Error in the input')
            elif n == '2':
                print('You have chosen exp in 3')
                while True:
                    a = input('Please enter number')
                    if check(a, float):
                        break
                    print('Error in the input')
            print('Result of the operation is {}'.format(exp[int(n) - 1](float(a))))
            return exp[int(n) - 1](float(a))
        if n == '2':
            n = input_from_numbers(root_str)
            if n == '1':
                print('You have chosen root in 3')
                while True:
                    a = input('Please enter number')
                    if check(a, float) and float(a) >= 0:
                        break
                    print('Error in the input')
            elif n == '2':
                print('You have chosen root in 2')
                while True:
                    a = input('Please enter number')
                    if check(a, float) and float(a) >= 0:
                        break
                    print('Error in the input')
            print('Result of the operation is {}'.format(round(root[int(n)-1](float(a)), 3)))
            return round(root[int(n)-1](float(a)), 3)


if __name__ == '__main__':
    main()
