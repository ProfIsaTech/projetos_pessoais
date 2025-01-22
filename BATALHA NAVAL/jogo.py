import random

# Tamanho do tabuleiro
tamanho = 5

# Criando tabuleiros para jogador e oponente
tabuleiro_jogador = [["~"] * tamanho for _ in range(tamanho)]
tabuleiro_oponente = [["~"] * tamanho for _ in range(tamanho)]
tabuleiro_oponente_visivel = [["~"] * tamanho for _ in range(tamanho)]

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))

print("Tabuleiro do Jogador:")
imprimir_tabuleiro(tabuleiro_jogador)


def posicionar_navios(tabuleiro, numero_navios):
    for _ in range(numero_navios):
        while True:
            linha = random.randint(0, tamanho - 1)
            coluna = random.randint(0, tamanho - 1)
            if tabuleiro[linha][coluna] == "~":
                tabuleiro[linha][coluna] = "N"
                break

# Posiciona 3 navios para o jogador e oponente
posicionar_navios(tabuleiro_jogador, 3)
posicionar_navios(tabuleiro_oponente, 3)


def posicionar_navios(tabuleiro, numero_navios):
    for _ in range(numero_navios):
        while True:
            linha = random.randint(0, tamanho - 1)
            coluna = random.randint(0, tamanho - 1)
            if tabuleiro[linha][coluna] == "~":
                tabuleiro[linha][coluna] = "N"
                break

# Posiciona 3 navios para o jogador e oponente
posicionar_navios(tabuleiro_jogador, 3)
posicionar_navios(tabuleiro_oponente, 3)


def posicionar_navios(tabuleiro, numero_navios):
    for _ in range(numero_navios):
        while True:
            linha = random.randint(0, tamanho - 1)
            coluna = random.randint(0, tamanho - 1)
            if tabuleiro[linha][coluna] == "~":
                tabuleiro[linha][coluna] = "N"
                break

# Posiciona 3 navios para o jogador e oponente
posicionar_navios(tabuleiro_jogador, 3)
posicionar_navios(tabuleiro_oponente, 3)


def posicionar_navios(tabuleiro, numero_navios):
    for _ in range(numero_navios):
        while True:
            linha = random.randint(0, tamanho - 1)
            coluna = random.randint(0, tamanho - 1)
            if tabuleiro[linha][coluna] == "~":
                tabuleiro[linha][coluna] = "N"
                break

# Posiciona 3 navios para o jogador e oponente
posicionar_navios(tabuleiro_jogador, 3)
posicionar_navios(tabuleiro_oponente, 3)


def posicionar_navios(tabuleiro, numero_navios):
    for _ in range(numero_navios):
        while True:
            linha = random.randint(0, tamanho - 1)
            coluna = random.randint(0, tamanho - 1)
            if tabuleiro[linha][coluna] == "~":
                tabuleiro[linha][coluna] = "N"
                break

# Posiciona 3 navios para o jogador e oponente
posicionar_navios(tabuleiro_jogador, 3)
posicionar_navios(tabuleiro_oponente, 3)


def posicionar_navios(tabuleiro, numero_navios):
    for _ in range(numero_navios):
        while True:
            linha = random.randint(0, tamanho - 1)
            coluna = random.randint(0, tamanho - 1)
            if tabuleiro[linha][coluna] == "~":
                tabuleiro[linha][coluna] = "N"
                break

# Posiciona 3 navios para o jogador e oponente
posicionar_navios(tabuleiro_jogador, 3)
posicionar_navios(tabuleiro_oponente, 3)
