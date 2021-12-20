n = 16


def copy_tuple(boolean):
    def wrap(func):
        def wrapper(*args):
            l = func(*args)
            if boolean:
                l_changed = []
                for i in l:
                    l_changed.append([(i[j], i[j + 1], i[j + 2], i[j + 3]) for j in range(0, len(i), 4)])

                return l_changed
            return l

        return wrapper

    return wrap


@copy_tuple(True)
def copybook(number, n):
    """Function to return lists of pages
    - number - number of pages in book
    - n - number of pages in copybook"""
    for j in range(0, number, n):
        l_copybook = []
        l = []
        l_copybook.append((j + n - i, j + i + 1, j + i + 2, j + n - (i + 1)) for i in range(0, int(n / 2), 2))
        for i in l_copybook:
            for q in i:
                l.extend(q)
        yield l


# @copy_tuple(True)
# def copybook(number, n):
#     """Function to return lists of pages
#     - number - number of pages in book
#     - n - number of pages in copybook"""
#     l = []
#     for j in range(0, number, n):
#         l_copybook = []
#         l.append([])
#         l_copybook.append((j + n - i, j + i + 1, j + i + 2, j + n - (i + 1)) for i in range(0, int(n / 2), 2))
#         for i in l_copybook:
#             for q in i:
#                 l[-1].extend(q)
#     return l


while True:
    num = input('Enter the number of pages')
    if num.isdigit() and int(num) <= 1280 and int(num) % n == 0:
        num = int(num)
        break
    print('This num can`t be, please try one more time.')
print('Copybooks number = {}'.format(num//n))
for i in copybook(num, n):
    for j in i:
        print(j)
# print(i for i in copybook(32, n))
