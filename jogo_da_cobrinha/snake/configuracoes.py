"""Dimensões do tabuleiro, velocidade e mapeamento de teclas."""

COLUNAS, LINHAS, CELULA = 30, 22, 24
INTERVALO = 130  # milissegundos por movimento
DIRECOES = {
    'Up': (0, -1), 'w': (0, -1),
    'Down': (0, 1), 's': (0, 1),
    'Left': (-1, 0), 'a': (-1, 0),
    'Right': (1, 0), 'd': (1, 0),
}

