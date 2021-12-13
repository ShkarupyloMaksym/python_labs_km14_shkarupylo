import time


def deck():
    cards = ['A', *range(2, 10), 'J', 'Q', 'K']
    for i in 'diamonds, clubs, hearts, spades'.split(', '):
        for j in cards:
            yield str(j)+' '+i

param=deck()
for i in param:
    print(i)

# StopIteration must be the last!
time.sleep(0.1)

next(param)