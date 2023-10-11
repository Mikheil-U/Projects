import random
import pyinputplus as pyip


class Game:
    """rock paper scissors game"""

    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.moves = {0: 'rock', 1: 'paper', 2: 'scissors'}

    def computer_play(self):
        random_num = random.randint(0, 2)
        return self.moves[random_num]

    def player_play(self):
        player_move = pyip.inputInt('Enter: \n1 rock. \n2 paper. \n3 scissors', lessThan=4, greaterThan=0)
        return self.moves[player_move - 1]

    def compare(self):
        pc = self.computer_play()
        pl = self.player_play()
        print(f"Computer: {pc}")
        if pc == pl:
            print('[DRAW]')
            self.show_scores()
        elif pc == 'scissors' and pl == 'paper':
            self.computer_score += 1
            print('[COMPUTER WON]')
            self.show_scores()
        elif pl == 'scissors' and pc == 'paper':
            self.player_score += 1
            print('[PLAYER WON]')
            self.show_scores()
        elif pc == 'rock' and pl == 'paper':
            self.player_score += 1
            print('[PLAYER WON]')
            self.show_scores()
        elif pl == 'rock' and pc == 'paper':
            self.computer_score += 1
            print('[COMPUTER WON]')
            self.show_scores()
        elif pl == 'scissors' and pc == 'rock':
            self.computer_score += 1
            print('[COMPUTER WON]')
            self.show_scores()
        elif pc == 'scissors' and pl == 'rock':
            self.player_score += 1
            print('[PLAYER WON]')
            self.show_scores()

    def show_scores(self):
        print(f'[Computer Score: {self.computer_score}; Player Score: {self.player_score}]')


if __name__ == '__main__':
    game = Game()
    num_of_matches = pyip.inputInt("Enter the winning score:")
    
    while True:
        if game.player_score == num_of_matches:
            print(f"Player Won With The Score of: {game.player_score}")
            break
        elif game.computer_score == num_of_matches:
            print(f"Computer Won With The Score of: {game.computer_score}")
            break
        else:
            print("Game Continues!")
            game.compare()
