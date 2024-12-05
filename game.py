import customtkinter as ctk
from tkinter import Text
from player import Player
from crypto import CryptoFactory
from chart import Chart
import random


class Game:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Trader de Criptomoedas")
        self.root.geometry("1000x800")  # Tamanho padrão (opcional, já que será maximizado)
        self.root.state("zoomed")  # Maximiza a janela automaticamente

        # Configuração inicial
        self.player = Player()
        self.crypto_factory = CryptoFactory()
        self.chart = Chart(self.root)
        self.current_crypto = None

        # Interface do jogo
        self.create_ui()




    def create_ui(self):
        # Título
        self.title_label = ctk.CTkLabel(self.root, text="Trader de Criptomoedas", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=10)

        # Exibição do valor da carteira
        self.wallet_label = ctk.CTkLabel(self.root, text=f"Carteira: R$ {self.player.wallet:.2f}", font=("Arial", 18, "italic"))
        self.wallet_label.pack(pady=10)

        # Texto de exibição (usando tkinter.Text para suportar cores e espaçamento)
        self.game_log = Text(
            self.root, 
            width=120, 
            height=15, 
            state="disabled", 
            wrap="word", 
            bg="#333", 
            fg="#fff", 
            font=("Consolas", 14),  # Fonte diferenciada para log
            spacing3=10  # Espaçamento entre as linhas
        )
        self.game_log.pack(pady=20)

        # Painel de Ações
        self.action_frame = ctk.CTkFrame(self.root)
        self.action_frame.pack(pady=10)

        # Linha superior: Começar e Recomeçar
        self.start_button = ctk.CTkButton(self.action_frame, text="Começar", command=self.start_game, width=120)
        self.start_button.grid(row=0, column=0, padx=15, pady=10)

        self.reset_button = ctk.CTkButton(self.action_frame, text="Recomeçar", command=self.reset_game, width=120)
        self.reset_button.grid(row=0, column=1, padx=15, pady=10)

        # Linha inferior: Subir e Descer
        self.up_button = ctk.CTkButton(self.action_frame, text="Subir", command=self.choose_up, width=120)
        self.up_button.grid(row=1, column=0, padx=15, pady=10)

        self.down_button = ctk.CTkButton(self.action_frame, text="Descer", command=self.choose_down, width=120)
        self.down_button.grid(row=1, column=1, padx=15, pady=10)

    def start_game(self):
        self.log_message("Jogo iniciado! Faça sua escolha para a primeira criptomoeda.", "info")
        self.player.reset()
        self.update_wallet_label()
        self.chart.reset_graph()
        self.next_round()

    def next_round(self):
        self.current_crypto = random.choice(self.crypto_factory.get_all_cryptos())
        self.log_message(f"Nova criptomoeda: {self.current_crypto.name}. Analise o gráfico!", "info")
        self.chart.update_graph(self.current_crypto)

    def choose_up(self):
        self.make_choice("up")

    def choose_down(self):
        self.make_choice("down")

    def make_choice(self, choice):
        if not self.current_crypto:
            self.log_message("Por favor, clique em 'Começar' para iniciar o jogo.", "info")
            return

        result = self.chart.determine_movement()
        if result == choice:
            self.player.add_to_wallet(self.current_crypto.value)
            self.log_message(f"Você acertou! Ganhou R$ {self.current_crypto.value:.2f}.", "success")
        else:
            if self.current_crypto.value > self.player.wallet:
                self.log_message(f"Você perdeu e sua carteira não tem saldo suficiente. Fim de jogo!", "error")
                self.reset_game()
                return
            else:
                self.player.remove_from_wallet(self.current_crypto.value)
                self.log_message(f"Você errou! Perdeu R$ {self.current_crypto.value:.2f}.", "error")
        self.update_wallet_label()
        self.next_round()  # Passa automaticamente para a próxima rodada

    def reset_game(self):
        """Reinicia o jogo sem encerrar o terminal."""
        self.player.reset()
        self.update_wallet_label()
        self.chart.reset_graph()
        self.game_log.configure(state="normal")
        self.game_log.delete("1.0", "end")
        self.game_log.configure(state="disabled")
        self.log_message("Jogo reiniciado! Clique em 'Começar' para iniciar novamente.", "info")
        self.current_crypto = None

    def update_wallet_label(self):
        self.wallet_label.configure(text=f"Carteira: R$ {self.player.wallet:.2f}")

    def log_message(self, message, message_type="info"):
        """
        Loga mensagens no terminal e no jogo.
        - message_type="success": Mensagem em verde.
        - message_type="error": Mensagem em vermelho.
        - message_type="info": Mensagem padrão.
        """
        colors = {"success": "green", "error": "red", "info": "white"}

        self.game_log.configure(state="normal")
        self.game_log.insert("end", f"{message}\n\n", message_type)  # Adiciona duas linhas de espaçamento
        self.game_log.configure(state="disabled")
        self.game_log.tag_configure("success", foreground=colors["success"], font=("Consolas", 14, "bold"))
        self.game_log.tag_configure("error", foreground=colors["error"], font=("Consolas", 14, "bold"))
        self.game_log.tag_configure("info", foreground=colors["info"], font=("Consolas", 14))

    def run(self):
        self.root.mainloop()
