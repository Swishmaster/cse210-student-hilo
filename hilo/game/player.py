#Player class to do things with the player
#from game.dealer import Dealer

class Player():
    def __init__(self):
        self.points = 300
        self.guess = True
        #self.dealer = Dealer()

    def player_move(self):
        guess = input("Higher or lower: [h/l]").lower()
        return guess

    def change_points(self):
        pass

    def print_points(self):
        print(f'Your score is: {self.points}')