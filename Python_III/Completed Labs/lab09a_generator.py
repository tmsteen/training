
from random import shuffle
def dealer():
    """
    This generator creates a deck of cards and shuffles it.  Then it
    deals one card on the first and all subsequent accesses.  The cards
    are represented by the numbers 2x through 14x where the number
    respresents the cards Two through Ace.  The x is also a number
    (0 - 3) which represents the suits clubs, diamonds, hearts and
    spades respectively.  So, for example, the number 112 represents the
    Jack of Hearts and the number 33 represents the Three of Spades.
    """

    deck = []
    for x in range(2, 15):
        for y in range(4):            
            deck.append(10 * x + y)
    shuffle(deck)
    for card in deck:
        yield(card)


cards = 5
ranks = ['', '', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
deal_card = dealer()
for a in range(cards):
    rank, suit = divmod(next(deal_card), 10)
    print(ranks[rank], 'of', suits[suit])

