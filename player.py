class Player:
    def __init__(self):
        self.wallet = 0  # Carteira começa com R$ 0,00

    def add_to_wallet(self, value):
        self.wallet += value

    def remove_from_wallet(self, value):
        self.wallet -= value

    def reset(self):
        self.wallet = 0
