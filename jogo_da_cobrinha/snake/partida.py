"""Estado e regras da partida; não depende de Tkinter."""

import random

from .configuracoes import COLUNAS, LINHAS


class Partida:
    """Regras independentes da interface, para facilitar testes e alterações."""

    def __init__(self):
        self.cobra = [(8, 11), (7, 11), (6, 11)]  # cabeça primeiro
        self.direcao = (1, 0)
        self.proxima_direcao = self.direcao
        self.virou = False
        self.obstaculos = ({(x, 5) for x in range(5, 11)}
                           | {(x, 16) for x in range(19, 25)}
                           | {(21, y) for y in range(8, 13)})
        self.pontos = 0
        self.fim = False
        self.mensagem = ''
        self.comida = self.sortear_comida()

    def sortear_comida(self):
        ocupadas = set(self.cobra) | self.obstaculos
        livres = [(x, y) for x in range(COLUNAS) for y in range(LINHAS)
                  if (x, y) not in ocupadas]
        return random.choice(livres) if livres else None

    def mudar_direcao(self, nova):
        # Aceita uma curva por movimento; impede inversões de 180 graus.
        oposta = (-self.direcao[0], -self.direcao[1])
        if not self.fim and not self.virou and nova not in (oposta, self.direcao):
            self.proxima_direcao = nova
            self.virou = True

    def avancar(self):
        if self.fim:
            return
        self.direcao = self.proxima_direcao
        self.virou = False
        x, y = self.cobra[0]
        dx, dy = self.direcao
        cabeca = (x + dx, y + dy)

        if not (0 <= cabeca[0] < COLUNAS and 0 <= cabeca[1] < LINHAS):
            self.mensagem = 'Você bateu na parede!'
        elif cabeca in self.obstaculos:
            self.mensagem = 'Você bateu em um obstáculo!'
        elif cabeca in self.cobra:
            # Inclui a ponta da cauda, antes de qualquer remoção.
            self.mensagem = 'Você mordeu a própria cauda!'
        else:
            self.cobra.insert(0, cabeca)
            if cabeca == self.comida:
                # Não remove a cauda: crescimento de exatamente uma unidade.
                self.pontos += 1
                self.comida = self.sortear_comida()
                if self.comida is None:
                    self.fim = True
                    self.mensagem = 'Vitória! Você preencheu o tabuleiro!'
            else:
                self.cobra.pop()  # mantém o comprimento quando não come
            return
        self.fim = True

