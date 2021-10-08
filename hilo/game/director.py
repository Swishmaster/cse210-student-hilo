# This is the director class

from game.dealer import Dealer
from game.player import Player

class Director:
    '''
    This class will direct when things are prompted
    and sent to the screen.
    '''

    def __init__(self):
        self.card = 0
        self.new_card = 0
        self.keep_playing = True
        self.dealer = Dealer()
        self.player = Player()

    def start_game(self):
        #starts the game
        self.card = self.dealer.get_card()
        while self.keep_playing:
            self.get_card()
            self.play_game()
            self.card = self.new_card
            check = self.check_end_game()
            if check == False:
                self.keep_playing = False
                print("You have lost.")
            else:
                again = self.playing_again()
                if again  == False:
                    self.keep_playing == False
                    print("Thanks for playing!")

    def get_card(self):
        print(f"The card is: {self.card[0]}")
    
    def get_new_card(self):
        self.new_card = self.dealer.new_card()
        print(f"Next card was: {self.new_card[0]}")

    def play_game(self):
        self.player.player_move()
        self.get_new_card()
        self.update_points()
        self.player.print_points()

    def playing_again(self):
        play_again = input("Keep Playing: [y/n] ").lower()
        print("")
        if play_again == "y":
            self.keep_playing = True
        else:
            self.keep_playing = False
        return self.keep_playing

    def update_points(self):
        if (self.card[1] < self.new_card[1] and self.player.guess == "h"):
            self.player.points += 100
        elif(self.card[1] > self.new_card[1] and self.player.guess == "l"):
            self.player.points += 100
        else:
            self.player.points -= 75

    def check_end_game(self):
        if self.player.points <= 0:
            return False
