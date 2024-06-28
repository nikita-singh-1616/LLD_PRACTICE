from LLD_CHESS.pieces import Pawn, King, Queen, Bishop, Rook, Knight


class BlackPlayer:
    def __init__(self):
        self.piece_set = {
            'pawns': [],
            'king': King('B'),
            'queen': Queen('B'),
            'rooks': [],
            'knights': [],
            'bishops': []
        }
        self.color = 'B'
        self.generate_pieces()

    def generate_pieces(self):
        for i in range(8):
            self.piece_set['pawns'].append(Pawn('B'))
        for i in range(2):
            self.piece_set['bishops'].append(Bishop('B'))
            self.piece_set['rooks'].append(Rook('B'))
            self.piece_set['knights'].append(Knight('B'))


class WhitePlayer:
    def __init__(self):
        self.piece_set = {
            'pawns': [],
            'king': King('W'),
            'queen': Queen('W'),
            'rooks': [],
            'knights': [],
            'bishops': []
        }
        self.color = 'W'
        self.generate_pieces()

    def generate_pieces(self):
        for i in range(8):
            self.piece_set['pawns'].append(Pawn('W'))
        for i in range(2):
            self.piece_set['bishops'].append(Bishop('W'))
            self.piece_set['rooks'].append(Rook('W'))
            self.piece_set['knights'].append(Knight('W'))
