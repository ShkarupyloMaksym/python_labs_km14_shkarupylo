#  ВАШ КОД ТУТ
def cons(head, tail=[]):
    tail.reverse()
    tail.append(head)
    tail.reverse()
    return tail


# ПЕРЕВІРКА
l = cons(3,
         cons(2,
              cons(1, [])))
print(f'cons result: {l}')

assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')


# ВАШ КОД ТУТ
def sum(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[-1] + sum(lst[:-1])


# ПЕРЕВІРКА

print('sum result:', sum(l))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')
