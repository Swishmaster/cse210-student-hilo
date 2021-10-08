#Class for the dealer
import random

class Dealer():
    '''
    This class makes it so the game gets a random
    card and saves that card.
    '''
    def __init__(self):
        self.deck = {"Ace": 1,"2": 2,"3": 3,"4": 4,"5": 5, "6": 6,"7": 7,"8": 8,"9": 9, "10": 10, "Jack": 11,"Queen": 12,"King": 13}
        self.old_card = 0
        self.card = 0

    def get_card(self):
        a = random.choice(list(self.deck.items()))
        self.old_card = a[1]
        return a

    def new_card(self):
        b = random.choice(list(self.deck.items()))
        self.card = b[1]
        return b
        