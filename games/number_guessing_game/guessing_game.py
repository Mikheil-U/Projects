import random
import pyinputplus as pyip

max_tries = 10

class GuessingGame:
    """Simple Number Guessing Game
    Rules:
    Player has 10 tries to guess the number,
    player is given some hints: "lower" and "higher".
    """
    def __init__(self, start=1, end=100):
        self.start = start
        self.end = end
        self.secret_num = self.generate_secret_num(start, end)

    def generate_secret_num(self, start, end):
        return random.randint(start, end)

    def get_player_num(self):
        player_num = pyip.inputNum(f"Enter an integer in the range: {self.start}-{self.end} (Enter -1 to quit.)")
        return player_num


if __name__ == '__main__':
    game = GuessingGame()
    secret_num = game.secret_num

    while True:
        if max_tries > 0:
            player_number = game.get_player_num()
            if player_number == secret_num:
                print(f"You Have Guessed the Number: {secret_num}")
                break
            elif player_number == -1:
                print("Thanks for Playing")
                break
            else:
                if player_number < secret_num:
                    print("Higher!")
                else:
                    print("Lower!")
        else:
            print(f"Out of Tries, The Secret Number Was: {secret_num}")
            break
        max_tries -= 1

