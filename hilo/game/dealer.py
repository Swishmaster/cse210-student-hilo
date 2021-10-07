#Class for the dealer
import random

class Dealer():
    '''
    This class makes it so the game gets a random
    card and saves that card.
    '''
    def __init__(self):
        self.deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    def get_card(self):
        return random.choice(self.deck)

    def new_card(self):
        return random.choice(self.deck)
        