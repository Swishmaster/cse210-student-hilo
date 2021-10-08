#Player class to do things with the player


class Player():
    def __init__(self):
        self.points = 300
        self.guess = True

    def player_move(self):
        guess = input("Higher or lower: [h/l]").lower()
        return guess

    def update_points(self, old_card, new_card):
        if old_card < new_card and self.guess == "l" or old_card > new_card and self.guess == "h":
            self.points += 100
        else:
            self.points -= 75

    def print_points(self):
        print(f'Your score is: {self.points}')