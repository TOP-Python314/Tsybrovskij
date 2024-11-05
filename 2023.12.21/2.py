def deck():
    suits = ['черви', 'бубны', 'пики', 'трефы']
    ranks = list(range(2, 15))
    
    for suit in suits:
        for rank in ranks:
            yield (rank, suit)
# >>> print(list(deck())[::13])
# [(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]