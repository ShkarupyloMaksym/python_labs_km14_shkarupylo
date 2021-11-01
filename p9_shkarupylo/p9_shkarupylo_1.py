import numpy as np
import itertools


def permutation(matrix):
    """
        The function generates arr, what consume of permutations of matrix + character (1 or -1)
    """
    number = ''
    for i in range(len(matrix)):
        number += str(i + 1)
    t = list(itertools.permutations(number, len(number)))
    p = []
    for i in t:
        w=i
        w=list(w)
        q = 0
        j = 1
        while j < len(i):
            if w[j] < w[j - 1]:
                a = w[j]
                w[j] = w[j-1]
                w[j - 1] = a
                j -= 2
                q += 1
            if j<1:
                j=1
            else:
                j += 1
        if q % 2 == 0:
            q = 1

        else:
            q = -1
        p += [[q] + [matrix[o][int(i[o]) - 1] for o in range(len(i))]]
    return p


def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size=(dim, dim))
    return matrix


def composition(mas):
    """
        The function returns array of compositions lists what comprises of arrs
    """
    mas_n = []
    for i in mas:
        comp = 1
        for j in i:
            comp *= j
        mas_n.append(comp)
    return mas_n


def sum_mas(mas):
    """
        The function returns sum of mas elements
    """
    sum = 0
    for i in mas:
        sum += i
    return sum


# Example of using permutations() method
dim = ''
while not dim.isnumeric() or dim=='0':
    dim = input('Enter the matrix size (integer>0) ')
matrix = random_matrix(int(dim))

print('The matrix determinate: ',sum_mas(composition(permutation(matrix))))
print(np.linalg.det(matrix)) # to compare the program result with right result
