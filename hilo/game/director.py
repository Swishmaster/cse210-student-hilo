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
        self.old_card = 0
        self.keep_playing = True
        self.dealer = Dealer()
        self.player = Player()

    def start_game(self):
        #starts the game
        self.card = self.dealer.get_card()
        while self.keep_playing == True:
            self.get_card()
            self.play_game()
            play_again = self.playing_again()
            if play_again == False:
                self.keep_playing == False

    def get_card(self):
        print(f"The card is: {self.card}")
    
    def get_new_card(self):
        new_card = self.dealer.new_card()
        print(f"Next card was: {new_card}")
        self.card = self.old_card
        self.card = new_card

    def play_game(self):
        guess = self.player.player_move()
        self.get_new_card()
        self.player.update_points(self.old_card, self.card)
        self.player.print_points()

    def playing_again(self):
        play_again = input("Keep Playing: [y/n] ").lower()
        print("")
        if play_again == "y":
            self.keep_playing = True
        else:
            self.keep_playing = False
        return self.keep_playing

    