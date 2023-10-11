
class Game:
    """Tic-Tac-Toe"""

    def __init__(self):
        self.player_one = None
        self.player_to = None
        self.board = {0: ' ', 1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ',
                      6: ' ', 7: ' ', 8: ' ', 9: ' '}

    def draw_board(self, symbol):
        print(f' | {self.board[symbol]}  |  {symbol} |  {symbol} |')
        print(f' | {symbol}  |  {symbol} |  {symbol} |')
        print(f' | {symbol}  |  {symbol} |  {symbol} |')

    def current_player_play(self):
        pass

    def check_board(self):
        pass


play = Game()
play.draw_board('X')


# print(f' | {symbol}  |  {symbol} |  {symbol} |')
# print(f' | {symbol}  |  {symbol} |  {symbol} |')
# print(f' | {symbol}  |  {symbol} |  {symbol} |')
