from LLD_TIC_TAC_TOE.board import GameBoard
from LLD_TIC_TAC_TOE.symbol import SymbolX, SymbolO
from LLD_TIC_TAC_TOE.user import User1, User2


class Game:
    def __init__(self):
        self.board = None
        self.player1 = None
        self.player2 = None
        self.queue = []
        self.board_size = None
        self.initialize_players()

    def initialize_players(self):
        name1 = input('Enter player1 name: ')
        name2 = input('Enter player2 name: ')
        x = SymbolX()
        o = SymbolO()
        self.player1 = User1(name1, x)
        self.player2 = User2(name2, o)
        self.queue = [self.player1, self.player2]
        self.initialize_board()

    def initialize_board(self):
        self.board_size = int(input('Enter the size of the board'))
        self.board = GameBoard(self.board_size)
        self.start()

    def start(self):
        counter = 0
        self.board.display()
        while counter < (self.board_size * self.board_size):
            cur_player = self.queue.pop(0)
            while True:
                row = int(input('Choose the row to place your piece'))
                col = int(input('Choose the col to place your piece'))
                if self.board.check_position(row, col):
                    self.board.place_piece(row, col, cur_player.symbol)
                    if self.board.check(row, col, cur_player.symbol):
                        print(f'{cur_player.name} has won the game')
                        return
                    break

                else:
                    print('Invalid Position')
            self.queue.append(cur_player)
            counter += 1
            print(counter)
            self.board.display()
        print('MATCH DRAW')
        return


Game()
