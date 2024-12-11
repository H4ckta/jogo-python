# README - Jogo Python com Design Patterns

## O que foi feito

Este projeto é um jogo simples que simula o mercado de criptomoedas. O código foi aprimorado com a integração de cinco padrões de design para melhorar a estrutura, escalabilidade e manutenção.

## Como executar

1. Certifique-se de ter o Python instalado (versão 3.8 ou superior).
2. Instale as dependências necessárias com:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o arquivo `main.py` para iniciar o jogo:
   ```bash
   python main.py
   ```

## Padrões de Projeto Utilizados

### Singleton
**Arquivo:** `chart.py`
- A classe `Chart` foi implementada como um Singleton, garantindo que apenas uma instância seja criada e usada em todo o projeto.
- **Benefício:** Evita conflitos ao trabalhar com múltiplos gráficos.

### Factory
**Arquivo:** `crypto.py`
- A `CryptoFactory` foi implementada para criar objetos `Crypto` centralizadamente.
- **Benefício:** Simplifica a criação de instâncias e melhora a manutenção.

### Observer
**Arquivo:** `crypto.py`
- A classe `Crypto` notifica todos os observadores registrados sempre que seu valor muda.
- **Benefício:** Facilita a atualização de gráficos e outros componentes dependentes de dados.

### Strategy
**Arquivo:** `crypto.py`
- Diferentes estratégias de cálculo de valores foram implementadas, como `RandomPricingStrategy` e `StablePricingStrategy`.
- **Benefício:** Permite flexibilidade e fácil troca de estratégias sem alterar a lógica principal.

### Command
**Arquivo:** `game.py`
- Comandos como `BuyCommand`, `SellCommand` e `UpdateMarketCommand` foram criados para encapsular ações específicas.
- **Benefício:** Facilita a adição de novas ações sem modificar o núcleo do jogo.
