from abc import ABC, abstractmethod

from LLD_CHESS.piece_set import BlackPlayer, WhitePlayer


class BoardInterface(ABC):
    def __init__(self, size):
        self.size = size
        self.board = None

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def move(self, position,next_position):
        pass


class ChessBoard(BoardInterface):
    def __init__(self):
        super().__init__(8)
        self.board = [['_' for _ in range(self.size)] for _ in range(self.size)]
        self.black = BlackPlayer()
        self.white = WhitePlayer()
        self.initialize()
        self.display()
        self.game()

    def initialize(self):
        """pawn initialization"""
        for i in range(8):
            self.board[1][i] = self.black.piece_set['pawns'][i]

        for i in range(8):
            self.board[6][i] = self.white.piece_set['pawns'][i]
        """rook initialization"""
        self.board[0][0] = self.black.piece_set['rooks'][0]
        self.board[0][self.size - 1] = self.black.piece_set['rooks'][1]
        self.board[self.size - 1][0] = self.white.piece_set['rooks'][0]
        self.board[self.size - 1][self.size - 1] = self.white.piece_set['rooks'][1]
        """knight initialization"""
        self.board[0][1] = self.black.piece_set['knights'][0]
        self.board[0][self.size - 2] = self.black.piece_set['knights'][1]
        self.board[self.size - 1][1] = self.white.piece_set['knights'][0]
        self.board[self.size - 1][self.size - 2] = self.white.piece_set['knights'][1]

        """bishop initialization"""
        self.board[0][2] = self.black.piece_set['bishops'][0]
        self.board[0][self.size - 3] = self.black.piece_set['bishops'][1]
        self.board[self.size - 1][2] = self.white.piece_set['bishops'][0]
        self.board[self.size - 1][self.size - 3] = self.white.piece_set['bishops'][1]

        """king initialization"""
        self.board[0][3] = self.black.piece_set['king']
        self.board[self.size - 1][3] = self.white.piece_set['king']

        """queen initialization"""
        self.board[0][4] = self.black.piece_set['queen']
        self.board[self.size - 1][4] = self.white.piece_set['queen']

    def display(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != '_':
                    print(self.board[i][j].name, end=" ")
                else:
                    print(self.board[i][j], end="  ")
            print()

    def game(self):
        toggle = True
        while True:
            if toggle:
                current_player = self.white
                print('Current Player is White')
            else:
                current_player = self.black
                print('Current Player is Black')

            x = int(input('select the x coordinate of the piece you want to move'))
            if x > self.size:
                print('Invalid X coordinate')
                continue
            y = int(input('select the y coordinate of the piece you want to move'))
            if y > self.size:
                print('Invalid Y coordinate')
                continue
            if self.board[x][y] == '_' or (self.board[x][y] != '_' and self.board[x][y].color != current_player.color):
                print('Invalid Position')
                continue
            else:
                self.board[x][y].position = [x,y]
                possible_moves = self.board[x][y].move(self.board)
                print(f'your possible moves are {possible_moves}')
                while True:
                    new_x = int(input('select the x coordinate of the piece you want to move to '))
                    if new_x > self.size:
                        print('Invalid X coordinate')
                        continue
                    new_y = int(input('select the y coordinate of the piece you want to move to '))
                    if new_y > self.size:
                        print('Invalid Y coordinate')
                        continue
                    if [new_x,new_y] not in possible_moves:
                        print('Invalid move')
                        continue
                    else:
                        self.move([x,y],[new_x,new_y])
                        toggle = not toggle
                        break

    def move(self, cur_pos,next_pos):
        self.board[cur_pos[0]][cur_pos[1]],self.board[next_pos[0]][next_pos[1]] = '_',self.board[cur_pos[0]][cur_pos[1]]
        self.display()


obj = ChessBoard()
# obj.display()
