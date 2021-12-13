def deck():
    cards = ['A', *range(2, 10), 'J', 'Q', 'K']
    suit = 'diamonds, clubs, hearts, spades'.split(', ')
    for i in suit:
        for j in cards:
            yield str(j) + ' ' + i


param = deck()
while param:
    print(next(param))
