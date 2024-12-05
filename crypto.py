import random

class Crypto:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.history = [value * random.uniform(0.8, 1.2) for _ in range(5)]  # Histórico inicial aleatório

    def get_price_history(self):
        return self.history

    def predict_price_movement(self):
        return random.choice(["up", "down"])

class CryptoFactory:
    def __init__(self):
        self.crypto_list = [
            Crypto("Bitcoin", 1000),
            Crypto("Ethereum", 500),
            Crypto("Cardano", 200),
            Crypto("XRP", 50),
            Crypto("Solana", 150),
            Crypto("Dogecoin", 25),
            Crypto("Polkadot", 300),
            Crypto("Litecoin", 400),
            Crypto("Binance Coin", 700),
            Crypto("Avalanche", 100),
        ]

    def get_all_cryptos(self):
        return self.crypto_list
