# Jogo de Trader de Criptomoedas

## Descrição do Jogo

Este é um jogo interativo de análise de tendências em que você é um trader de criptomoedas. O objetivo é analisar gráficos gerados aleatoriamente e decidir se o valor de uma criptomoeda vai **subir** ou **descer**. O jogo se adapta a cada rodada, tornando-se mais desafiador com a análise de médias ponderadas.

### Como Jogar

1. Clique em **Começar** para iniciar o jogo.
2. Um gráfico será exibido com os preços de uma criptomoeda selecionada aleatoriamente.
3. Analise o gráfico e escolha se o preço vai **Subir** ou **Descer**.
4. Se acertar:
   - O valor da criptomoeda será adicionado à sua carteira.
5. Se errar:
   - O valor será subtraído da carteira.
   - Caso o valor da carteira seja insuficiente, o jogo termina.

---

## Configuração do Projeto

### Dependências

Certifique-se de instalar as bibliotecas necessárias:

```bash
pip install customtkinter matplotlib colorama
```

#### Estrutura de Arquivos
.
├── main.py           # Arquivo principal do jogo
├── game.py           # Lógica principal e interface do jogo
├── player.py         # Gerenciamento da carteira do jogador
├── crypto.py         # Configuração das criptomoedas
├── chart.py          # Geração de gráficos e lógica de tendências
└── README.md         # Arquivo de documentação


#### Padrões de Design Utilizados

1. Strategy
O padrão Strategy é utilizado para implementar a lógica de subida ou descida dos preços. A escolha do jogador é comparada à movimentação determinada pelo gráfico.

2. Factory
O padrão Factory é aplicado na criação das criptomoedas. A classe CryptoFactory é responsável por gerar as instâncias de criptomoedas utilizadas no jogo.

3. Observer
O padrão Observer é aplicado para atualizar a interface do jogo. Quando o jogador faz uma escolha ou uma nova criptomoeda é sorteada, os gráficos e a carteira são atualizados dinamicamente.

### Fluxograma do Jogo

O fluxo do jogo pode ser representado pelo seguinte diagrama:

+----------------------+
| Início do Jogo       |
+----------+-----------+
           |
           v
+----------------------+            +----------------------+
| Sorteia uma Criptomoeda |---->----| Gera o Gráfico       |
+----------+-----------+            +----------+-----------+
           |                                    |
           | Escolha do Jogador                |
           | Subir / Descer                    |
           v                                    v
+----------------------+            +----------------------+
| Determina Movimento   |<--+---<---| Analisa o Gráfico    |
+----------+-----------+            +----------+-----------+
           |                                    |
           | Acertou                            | Errou
           v                                    v
+----------------------+            +----------------------+
| Atualiza Carteira     |            | Subtrai ou Finaliza |
+----------+-----------+            +----------+-----------+
           |                                    |
           +------------------------------------+
                       Próxima Rodada


### Como Executar o Jogo

1. Certifique-se de que todos os arquivos necessários estão no mesmo diretório.
2. Execute o arquivo principal do jogo:
```bash
python main.py
```
3. Divirta-se jogando!