from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, name):
        self.name = name
        self.color = None
        self.status = True
        self.position = None

    @abstractmethod
    def move(self, board):
        pass


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(f'{color}P')
        self.color = color
        self.status = True

    def move(self, board):
        possible_positions = []
        if self.color == 'W' and self.position[0] != 0:
            if board[self.position[0] - 1][self.position[1]] == '_':
                possible_positions.append([self.position[0] - 1, self.position[1]])

            if (board[self.position[0] - 1][self.position[1] - 1] != '_' and
                    board[self.position[0] - 1][self.position[1] - 1].color != self.color and
                    self.position[1] > 0):
                possible_positions.append([self.position[0] - 1, self.position[1] - 1])
            if (self.position[1] < len(board[0]) - 1 and board[self.position[0] - 1][self.position[1] + 1] != '_' and
                    board[self.position[0] - 1][self.position[1] + 1].color != self.color):
                possible_positions.append([self.position[0] - 1, self.position[1] + 1])
            if self.position[0] == len(board) - 2 and board[self.position[0] - 2][self.position[1]] == '_':
                possible_positions.append([self.position[0] - 2, self.position[1]])
        if self.color == 'B' and self.position[0] != len(board) - 1:
            if board[self.position[0] + 1][self.position[1]] == '_':
                possible_positions.append([self.position[0] + 1, self.position[1]])
            if (board[self.position[0] + 1][self.position[1] - 1] != '_' and
                    board[self.position[0] + 1][self.position[1] - 1].color != self.color and
                    self.position[1] > 0):
                possible_positions.append([self.position[0] + 1, self.position[1] - 1])
            if (self.position[1] < len(board[0]) - 1 and board[self.position[0] + 1][self.position[1] + 1] != '_' and
                    board[self.position[0] + 1][self.position[1] + 1].color != self.color):
                possible_positions.append([self.position[0] + 1, self.position[1] + 1])
            if self.position[0] == 1 and board[3][self.position[1]] == '_':
                possible_positions.append([3, self.position[1]])
        return possible_positions


class King(Piece):
    def __init__(self, color):
        super().__init__(f'{color}K')
        self.color = color

    def move(self):
        pass


class Queen(Piece):
    def __init__(self, color):
        super().__init__(f'{color}Q')
        self.color = color

    def move(self):
        pass


class Rook(Piece):
    def __init__(self, color):
        super().__init__(f'{color}R')
        self.color = color

    def move(self):
        pass


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(f'{color}B')
        self.color = color

    def move(self,board):
        n = len(board)
        possible_moves = []
        # left top diagonal
        i = self.position[0]-1
        j = self.position[1]-1
        while i >= 0 and j>=0 and i<n and j<n and (board[i][j]=='_' or board[i][j].color!=self.color):
            possible_moves.append([i, j])
            if board[i][j]!='_':
                break
            j-=1
            i-=1
        # right top diagonal
        i = self.position[0]-1
        j = self.position[1]+1
        while i >= 0 and j >= 0 and i < n and j < n  and (board[i][j]=='_' or board[i][j].color!=self.color):
            possible_moves.append([i, j])
            if board[i][j]!='_':
                break
            j += 1
            i -= 1
        # left top diagonal
        i = self.position[0]+1
        j = self.position[1]-1
        while i >= 0 and j >= 0 and i < n and j < n and (board[i][j]=='_' or board[i][j].color!=self.color):
            possible_moves.append([i, j])
            if board[i][j]!='_':
                break
            j -= 1
            i += 1
        # left top diagonal
        i = self.position[0]+1
        j = self.position[1]+1
        while i >= 0 and j >= 0 and i < n and j < n and (board[i][j]=='_' or board[i][j].color!=self.color):
            possible_moves.append([i, j])
            if board[i][j]!='_':
                break
            j += 1
            i += 1
        return possible_moves






class Knight(Piece):
    def __init__(self, color):
        super().__init__(f'{color}N')
        self.color = color

    def move(self, board):
        moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
        possible_moves = []
        for move in moves:
            x = self.position[0]
            y = self.position[1]
            new_x = x + move[0]
            new_y = y + move[1]
            if new_x >= 0 and new_x < len(board) and new_y >= 0 and new_y < len(board[0]):
                if board[new_x][new_y] == '_' or board[new_x][new_y].color != self.color:
                    possible_moves.append([new_x, new_y])
        return possible_moves
