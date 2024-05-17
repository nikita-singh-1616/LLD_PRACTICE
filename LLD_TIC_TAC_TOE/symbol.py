class Symbol:
    def __init__(self, symbol):
        self.name = symbol


class SymbolX(Symbol):
    def __init__(self):
        super().__init__('X')


class SymbolO(Symbol):
    def __init__(self):
        super().__init__('O')


class SymbolFactory:
    def __init__(self):
        self.hash_ = {
            'X': SymbolX(),
            'O': SymbolO()
        }

    def factory(self, inp):
        return self.hash_[inp]
