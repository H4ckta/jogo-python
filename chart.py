import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

class Chart:
    def __init__(self, root):
        self.root = root
        self.fig, self.ax = plt.subplots(figsize=(7, 4))
        self.canvas = None
        self.current_prices = []  # Armazena os preços gerados aleatoriamente

    def generate_prices(self, initial_value):
        """Gera preços aleatórios baseados em um valor inicial."""
        prices = [initial_value]
        for _ in range(4):  # Gerar 4 pontos adicionais para o gráfico
            change = random.uniform(-0.1, 0.1)  # Mudança percentual aleatória
            new_price = prices[-1] * (1 + change)
            prices.append(round(new_price, 2))  # Arredondar para duas casas decimais
        self.current_prices = prices

    def plot_graph(self, crypto):
        """Plota o gráfico para uma criptomoeda específica."""
        initial_value = crypto.value
        self.generate_prices(initial_value)  # Gera preços aleatórios
        self.ax.clear()
        self.ax.plot(self.current_prices, marker="o", label=f"{crypto.name}")
        self.ax.set_title(f"Tendência de {crypto.name}")
        self.ax.set_ylabel("Preço (USD)")
        self.ax.set_xlabel("Tempo")
        self.ax.legend()
        if self.canvas is None:
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
            self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    def update_graph(self, crypto):
        self.plot_graph(crypto)

    def reset_graph(self):
        self.ax.clear()
        self.current_prices = []
        if self.canvas:
            self.canvas.draw()

    def determine_movement(self):
        """Determina se o preço subiu ou desceu com base na média ponderada do histórico."""
        if len(self.current_prices) < 2:
            return "neutral"  # Não há dados suficientes
        avg_change = sum(self.current_prices[i] * (i + 1) for i in range(len(self.current_prices))) / sum(
            range(1, len(self.current_prices) + 1)
        )
        return "up" if avg_change > self.current_prices[-1] else "down"
