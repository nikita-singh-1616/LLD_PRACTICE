from LLD_TIC_TAC_TOE.board import GameBoard
from LLD_TIC_TAC_TOE.symbol import Symbol
from LLD_TIC_TAC_TOE.user import User1, User2, User


class Game:
    def __init__(self):
        self.board = None
        self.no_of_players = 0
        self.queue = []
        self.board_size = None
        self.symbols = []
        self.initialize_board()

    def initialize_players(self):
        self.no_of_players = int(input(f'enter the number of players(max {self.board_size ** 2}): '))
        while self.no_of_players > self.board_size ** 2:
            self.no_of_players = int(input(f'enter the number of players({self.board_size ** 2}): '))
        for i in range(self.no_of_players):
            name1 = input(f'Enter player{i + 1} name: ')
            symbol = input(f'enter their symbol: ')
            while symbol in self.symbols:
                symbol = input(f'enter their symbol: ')
            self.symbols.append(symbol)
            symbol = Symbol(symbol)
            player = User(name1, symbol)
            self.queue.append(player)
        self.start()

    def initialize_board(self):
        self.board_size = int(input('Enter the size of the board'))
        self.board = GameBoard(self.board_size)
        self.initialize_players()


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
