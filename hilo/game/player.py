#Player class to do things with the player
from game.dealer import Dealer

class Player():
    def __init__(self):
        self.points = 300
        self.guess = True
        self.dealer = Dealer()

    def player_move(self):
        self.guess = input("Higher or lower: [h/l]").lower()

    # def update_points(self):
    #     if (self.dealer.old_card <= self.dealer.card and self.guess == "l"):
    #         self.points += 100
    #     elif(self.dealer.old_card >= self.dealer.card and self.guess == "h"):
    #         self.points += 100
    #     else:
    #         self.points -= 75

    def print_points(self):
        print(f'Your score is: {self.points}')