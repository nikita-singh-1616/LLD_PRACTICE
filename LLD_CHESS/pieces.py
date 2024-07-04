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

    def move(self, board):
        x = self.position[0]
        y = self.position[1]
        top = [x + 1, y] if x + 1 < len(board) and (
                board[x + 1][y] == '_' or board[x + 1][y].color != self.color) else []
        bottom = [x - 1, y] if x - 1 >= 0 and (board[x - 1][y] == '_' or board[x - 1][y].color != self.color) else []
        right = [x, y + 1] if y + 1 < len(board[0]) and (
                    board[x][y + 1] == '_' or board[x][y + 1].color != self.color) else []
        left = [x, y - 1] if y - 1 >= 0 and (board[x][y - 1] == '_' or board[x][y - 1].color != self.color) else []
        possible_moves = top + left + right + bottom
        return possible_moves

    def check_for_check(self,board):
        x = self.position[0]
        y = self.position[1]
        """check for pawns"""
        if self.color == 'W':
            if ((board[x-1][y+1] != '_' and board[x-1][y+1].color!=self.color and board[x-1][y+1].name[-1] == 'P') or
                    (board[x-1][y-1] != '_' and board[x-1][y-1].color!=self.color and board[x-1][y-1].name[-1] == 'P')):
                return True
        if self.color == 'B':
            if ((board[x+1][y+1] != '_' and board[x+1][y+1].color!=self.color and board[x + 1][y + 1].name[-1] == 'P')
                    or (board[x+1][y-1] != '_' and board[x+1][y-1].color!=self.color) and board[x+1][y-1].name[-1]=='P'):
                return True
        """check for rook"""
        top_x = x - 1
        bot_x = x + 1
        while top_x >= 0:
            if board[top_x][y] == '_':
                top_x -= 1
            else:
                if board[top_x][y].color != self.color:
                    if board[top_x][y].name[-1] == 'R' or board[top_x][y].name[-1] == 'Q':
                        return True
                break

        while bot_x < len(board):
            if board[bot_x][y] == '_':
                bot_x += 1
            else:
                if board[bot_x][y].color != self.color:
                    if  board[bot_x][y].name[-1] == 'R' or board[bot_x][y].name[-1] == 'Q':

                        return True
                break
        #             horizontal movement
        right_y = y + 1
        left_y = y - 1
        while right_y < len(board[0]):
            if board[x][right_y] == '_':
                right_y += 1
            else:
                if board[x][right_y].color != self.color:
                    if board[x][right_y].name[-1] == 'R' or board[x][right_y].name[-1] == 'Q':
                        return True
                break

        while left_y >= 0:
            if board[x][left_y] == '_':
                left_y -= 1
            else:
                if board[x][left_y].color != self.color:
                    if board[x][left_y].name[-1] == 'R' or board[x][left_y].name[-1] == 'Q':
                        return True
                break
        moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
        for move in moves:
            x = self.position[0]
            y = self.position[1]
            new_x = x + move[0]
            new_y = y + move[1]
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                if board[new_x][new_y] != '_' and board[new_x][new_y].color != self.color:
                    if board[new_x][new_y].name[-1] == 'N':
                        return True
        return False

class Queen(Piece):
    def __init__(self, color):
        super().__init__(f'{color}Q')
        self.color = color

    def move(self, board):
        possible_moves = []
        n = len(board)
        cur_x = self.position[0]
        cur_y = self.position[1]
        #         vertical movement
        top_x = cur_x - 1
        bot_x = cur_x + 1
        while top_x >= 0:
            if board[top_x][cur_y] == '_':
                possible_moves.append([top_x, cur_y])
                top_x -= 1
            else:
                if board[top_x][cur_y].color != self.color:
                    possible_moves.append([top_x, cur_y])
                break

        while bot_x < len(board):
            if board[bot_x][cur_y] == '_':
                possible_moves.append([bot_x, cur_y])
                bot_x += 1
            else:
                if board[bot_x][cur_y].color != self.color:
                    possible_moves.append([bot_x, cur_y])
                break
        #             horizontal movement
        right_y = cur_y + 1
        left_y = cur_y - 1
        while right_y < len(board[0]):
            if board[cur_x][right_y] == '_':
                possible_moves.append([cur_x, right_y])
                right_y += 1
            else:
                if board[cur_x][right_y].color != self.color:
                    possible_moves.append([cur_x, right_y])
                break

        while left_y >= 0:
            if board[cur_x][left_y] == '_':
                possible_moves.append([cur_x, left_y])
                left_y -= 1
            else:
                if board[cur_x][left_y].color != self.color:
                    possible_moves.append([cur_x, left_y])
                break

        i = self.position[0] - 1
        j = self.position[1] - 1
        while 0 <= i < n and 0 <= j < n and (board[i][j] == '_' or board[i][j].color != self.color):
            possible_moves.append([i, j])
            if board[i][j] != '_':
                break
            j -= 1
            i -= 1
        # right top diagonal
        i = self.position[0] - 1
        j = self.position[1] + 1
        while 0 <= i < n and 0 <= j < n and (board[i][j] == '_' or board[i][j].color != self.color):
            possible_moves.append([i, j])
            if board[i][j] != '_':
                break
            j += 1
            i -= 1
        # left top diagonal
        i = self.position[0] + 1
        j = self.position[1] - 1
        while 0 <= i < n and 0 <= j < n and (board[i][j] == '_' or board[i][j].color != self.color):
            possible_moves.append([i, j])
            if board[i][j] != '_':
                break
            j -= 1
            i += 1
        # left top diagonal
        i = self.position[0] + 1
        j = self.position[1] + 1
        while 0 <= i < n and 0 <= j < n and (board[i][j] == '_' or board[i][j].color != self.color):
            possible_moves.append([i, j])
            if board[i][j] != '_':
                break
            j += 1
            i += 1
        return possible_moves


class Rook(Piece):
    def __init__(self, color):
        super().__init__(f'{color}R')
        self.color = color

    def move(self, board):
        possible_moves = []
        cur_x = self.position[0]
        cur_y = self.position[1]
        #         vertical movement
        top_x = cur_x - 1
        bot_x = cur_x + 1
        while top_x >= 0:
            if board[top_x][cur_y] == '_':
                possible_moves.append([top_x, cur_y])
                top_x -= 1
            else:
                if board[top_x][cur_y].color != self.color:
                    possible_moves.append([top_x, cur_y])
                break

        while bot_x < len(board):
            if board[bot_x][cur_y] == '_':
                possible_moves.append([bot_x, cur_y])
                bot_x += 1
            else:
                if board[bot_x][cur_y].color != self.color:
                    possible_moves.append([bot_x, cur_y])
                break
        #             horizontal movement
        right_y = cur_y + 1
        left_y = cur_y - 1
        while right_y < len(board[0]):
            if board[cur_x][right_y] == '_':
                possible_moves.append([cur_x, right_y])
                right_y += 1
            else:
                if board[cur_x][right_y].color != self.color:
                    possible_moves.append([cur_x, right_y])
                break
        while left_y >= 0:
            if board[cur_x][left_y] == '_':
                possible_moves.append([cur_x, left_y])
                left_y -= 1
            else:
                if board[cur_x][left_y].color != self.color:
                    possible_moves.append([cur_x, left_y])
                break
        return possible_moves


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(f'{color}B')
        self.color = color

    def move(self, board):
        n = len(board)
        possible_moves = []
        # left top diagonal
        i = self.position[0] - 1
        j = self.position[1] - 1
        while 0 <= i < n and 0 <= j < n and (board[i][j] == '_' or board[i][j].color != self.color):
            possible_moves.append([i, j])
            if board[i][j] != '_':
                break
            j -= 1
            i -= 1
        # right top diagonal
        i = self.position[0] - 1
        j = self.position[1] + 1
        while 0 <= i < n and 0 <= j < n and (board[i][j] == '_' or board[i][j].color != self.color):
            possible_moves.append([i, j])
            if board[i][j] != '_':
                break
            j += 1
            i -= 1
        # left top diagonal
        i = self.position[0] + 1
        j = self.position[1] - 1
        while 0 <= i < n and 0 <= j < n and (board[i][j] == '_' or board[i][j].color != self.color):
            possible_moves.append([i, j])
            if board[i][j] != '_':
                break
            j -= 1
            i += 1
        # left top diagonal
        i = self.position[0] + 1
        j = self.position[1] + 1
        while 0 <= i < n and 0 <= j < n and (board[i][j] == '_' or board[i][j].color != self.color):
            possible_moves.append([i, j])
            if board[i][j] != '_':
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
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                if board[new_x][new_y] == '_' or board[new_x][new_y].color != self.color:
                    possible_moves.append([new_x, new_y])
        return possible_moves
