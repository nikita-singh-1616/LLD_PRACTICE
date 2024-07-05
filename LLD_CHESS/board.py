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
            self.black.piece_set['pawns'][i].position = [1,i]

        for i in range(8):
            self.board[6][i] = self.white.piece_set['pawns'][i]
            self.white.piece_set['pawns'][i].position = [6,i]

        """rook initialization"""
        self.board[0][0] = self.black.piece_set['rooks'][0]
        self.black.piece_set['rooks'][0].position = [0,0]
        self.board[0][self.size - 1] = self.black.piece_set['rooks'][1]
        self.black.piece_set['rooks'][1].position = [0,self.size - 1]
        self.board[self.size - 1][0] = self.white.piece_set['rooks'][0]
        self.white.piece_set['rooks'][0].position = [self.size - 1,0]
        self.board[self.size - 1][self.size - 1] = self.white.piece_set['rooks'][1]
        self.white.piece_set['rooks'][1].position = [self.size - 1,self.size - 1]

        """knight initialization"""
        self.board[0][1] = self.black.piece_set['knights'][0]
        self.black.piece_set['knights'][0].position = [0,1]
        self.board[0][self.size - 2] = self.black.piece_set['knights'][1]
        self.black.piece_set['knights'][1].position = [0,self.size - 2]
        self.board[self.size - 1][1] = self.white.piece_set['knights'][0]
        self.white.piece_set['knights'][0].position = [self.size - 1,1]
        self.board[self.size - 1][self.size - 2] = self.white.piece_set['knights'][1]
        self.white.piece_set['knights'][1].position = [self.size - 1,self.size - 2]

        """bishop initialization"""
        self.board[0][2] = self.black.piece_set['bishops'][0]
        self.black.piece_set['bishops'][0].position = [0,2]
        self.board[0][self.size - 3] = self.black.piece_set['bishops'][1]
        self.black.piece_set['bishops'][1].position = [0,self.size - 3]
        self.board[self.size - 1][2] = self.white.piece_set['bishops'][0]
        self.white.piece_set['bishops'][0].position = [self.size - 1,2]
        self.board[self.size - 1][self.size - 3] = self.white.piece_set['bishops'][1]
        self.white.piece_set['bishops'][1].position = [self.size - 1,self.size - 3]

        """king initialization"""
        self.board[0][3] = self.black.piece_set['king']
        self.black.piece_set['king'].position = [0,3]
        self.board[self.size - 1][3] = self.white.piece_set['king']
        self.white.piece_set['king'].position = [self.size - 1,3]

        """queen initialization"""
        self.board[0][4] = self.black.piece_set['queen']
        self.black.piece_set['queen'] = [0,4]
        self.board[self.size - 1][4] = self.white.piece_set['queen']
        self.white.piece_set['queen'] = [self.size - 1,4]

    def display(self):
        print(" ",end=" ")
        for i in range(self.size):
            print(i,end='  ')
        print()

        for i in range(self.size):
            print(i,end=" ")
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
                        prev_state_1 = self.board[x][y]
                        prev_state_2 = self.board[new_x][new_y]
                        self.move([x,y],[new_x,new_y])
                        if self.check_for_check(current_player.color):
                            self.board[x][y] = prev_state_1
                            self.board[new_x][new_y] = prev_state_2
                            print('check alert')
                            self.display()
                            break
                        toggle = not toggle
                        break

    def move(self, cur_pos,next_pos):
        self.board[cur_pos[0]][cur_pos[1]],self.board[next_pos[0]][next_pos[1]] = '_',self.board[cur_pos[0]][cur_pos[1]]
        if self.board[next_pos[0]][next_pos[1]] != '_':
            self.board[next_pos[0]][next_pos[1]].status = False
        self.board[next_pos[0]][next_pos[1]].position = [next_pos[0],next_pos[1]]
        self.display()

    def check_for_check(self,cur_color):
        if self.black.piece_set['king'].check_for_check(self.board):
            print('CHECK FOR BLACK')
            return cur_color == self.black.color
        if self.white.piece_set['king'].check_for_check(self.board):
            print('CHECK FOR WHITE')
            return cur_color == self.white.color



obj = ChessBoard()
# obj.display()
