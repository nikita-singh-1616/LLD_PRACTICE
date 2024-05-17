class User:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class User1(User):
    def __init__(self,name,symbol):
        super().__init__(name,symbol)


class User2(User):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)
