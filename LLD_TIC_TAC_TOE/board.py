class GameBoard:
    def __init__(self, size):
        self.size = size
        self.board = [['_' for i in range(size)] for j in range(size)]

    def display(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if self.board[i][j] != '_':
                    row.append(self.board[i][j].name)
                else:
                    row.append(self.board[i][j])
            print(row)

    def check_position(self, i, j):
        return self.board[i][j] == '_'

    def place_piece(self, i, j, piece):
        self.board[i][j] = piece

    def check(self, i, j, piece):
        row = self.board[i][:]
        col = []
        diag1 = []
        diag2 = []
        for x in range(self.size):
            diag1.append(self.board[x][x])
            diag2.append(self.board[x][self.size - x - 1])

        for x in range(self.size):
            col.append(self.board[x][j])
        if (len(set(row)) == 1 and row[0] == piece) or (len(set(col)) == 1 and col[0] == piece) or (
                len(set(diag1)) == 1 and diag1[0] == piece) or (len(set(diag2)) == 1 and diag2[0] == piece):
            return True
        else:
            return False
