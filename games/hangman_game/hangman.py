import random
import pyinputplus as pyip

"""
 * Store words in a txt or csv file.
 * Pick a word randomly from the base of words.
 * Determine the length of the word.
 * Ask players for their guesses, if correct -> place letter(s) on an empty slot.
 *
"""


class Hangman:
    """
    Simple Hangman Game. A word is randomly picked from a list of words(saved locally).
    Keeps Track of total points, game can be played single or multiple times.
    """
    def __init__(self):
        self.words_li = []  # holds the words list, later it will be used to randomly pick a word for a secret word
        self.text_file = "words_list.txt"  #
        self.secret_word = "hello"
        self.table = []  # to draw a table
        self.read_file()  # reads words list from text file
        #self.pick_random_word()  # randomly picks a word
        self.player_guess = ""  # to hold players single character
        self.tries_left = 6  # tries left till the game is finished
        self.already_picked_letters = []  # to keep track of what letters a player entered
        self.draw_state_counter = 0  # this is used to draw a hangman picture when letter doesn't match
        self.correct_matches = []

    def read_file(self):
        with open(self.text_file) as file:
            for line in file:
                self.words_li.append(line.strip())

    def pick_random_word(self):
        self.secret_word = self.words_li[random.randint(0, len(self.words_li)-1)]

    def draw_table(self):
        for i in range(len(self.secret_word)):
            self.table.append('_')
            print(self.table[i], end=' ')
        print()

    def modify_table(self):
        if self.is_matched():
            print("***[Letter Matched]***")
            for i in (self.get_indexes(self.player_guess)):
                self.table[i] = self.player_guess
                self.correct_matches.append(self.player_guess)

        else:
            self.tries_left -= 1
            print("***[No Match]***")
            self.draw_hangman_state(self.draw_state_counter)
            self.draw_state_counter += 1
        self.draw_table()

    def prompt_player(self):
        self.player_guess = pyip.inputStr("Enter a single character: ")

        while True:
            if self.player_guess in self.already_picked_letters:
                print("You already have chosen that letter? ")
                self.player_guess = pyip.inputStr("Enter a single character: ")
            else:
                self.already_picked_letters.append(self.player_guess)
                break

    def get_indexes(self, character: str):
        indexes = []
        for i in range(len(self.secret_word)):
            if character == self.secret_word[i]:
                indexes.append(i)
        return indexes

    def is_matched(self):
        if len(self.get_indexes(self.player_guess)) > 0:
            return True
        return False

    def draw_hangman_state(self, state: int):
        drawings_list = ["hangman_drawings//hangman_post.txt", "hangman_drawings//hangman_head.txt",
                         "hangman_drawings//hangman_body.txt", "hangman_drawings//hangman_left_leg.txt",
                         "hangman_drawings//hangman_right_leg.txt", "hangman_drawings//hangman_left_hand.txt",
                         "hangman_drawings//hangman_right_hand.txt"]

        draw = open(drawings_list[state])
        print(draw.read())


if __name__ == "__main__":
    play_again = 'YES'

    while play_again == 'yes' or play_again == 'YES':
        game = Hangman()
        game.draw_table()

        while game.tries_left >= 0:

            if game.tries_left < 1:
                game.draw_hangman_state(-1)
                print(f"You Lose! The Secret Word was: {game.secret_word}")
                break
            else:
                print(game.correct_matches == list(game.secret_word))
                if game.correct_matches == list(game.secret_word):
                    print("*********You Won!************")
                    break
                else:
                    game.prompt_player()
                    game.modify_table()
        play_again = pyip.inputYesNo("Play Again? y/n")
