"""Verifica as regras públicas sem depender da interface gráfica."""
import unittest
from snake.partida import Partida
from snake.configuracoes import COLUNAS, LINHAS


class TestPartida(unittest.TestCase):
    def test_comida_cresce_uma_unidade(self):
        p = Partida()
        tamanho = len(p.cobra)
        p.comida = (9, 11)
        p.avancar()
        self.assertEqual(len(p.cobra), tamanho + 1)
        self.assertEqual(p.pontos, 1)
        self.assertNotIn(p.comida, set(p.cobra) | p.obstaculos)

    def test_movimento_sem_comida_preserva_tamanho(self):
        p = Partida()
        p.comida = (0, 0)
        p.avancar()
        self.assertEqual(p.cobra, [(9, 11), (8, 11), (7, 11)])
        self.assertEqual(p.pontos, 0)

    def test_colisoes_encerram_sem_mover(self):
        casos = [
            ([(29, 0), (28, 0)], (1, 0), set()),
            ([(4, 5), (3, 5)], (1, 0), {(5, 5)}),
            ([(2, 2), (2, 3), (1, 3), (1, 2)], (-1, 0), set()),
            ([(2, 2), (2, 3), (1, 3), (1, 2), (1, 1)], (-1, 0), set()),
        ]
        for corpo, direcao, obstaculos in casos:
            with self.subTest(corpo=corpo):
                p = Partida()
                p.cobra = corpo.copy()
                p.direcao = p.proxima_direcao = direcao
                p.obstaculos = obstaculos
                p.avancar()
                self.assertTrue(p.fim)
                self.assertEqual(p.cobra, corpo)
                p.avancar()
                self.assertEqual(p.cobra, corpo)

    def test_bloqueia_inversao_e_duas_curvas_no_mesmo_passo(self):
        p = Partida()
        p.mudar_direcao((-1, 0))
        self.assertEqual(p.proxima_direcao, (1, 0))
        p.mudar_direcao((0, -1))
        p.mudar_direcao((-1, 0))
        p.avancar()
        self.assertEqual(p.cobra[0], (8, 10))
        p.mudar_direcao((-1, 0))
        p.avancar()
        self.assertEqual(p.cobra[0], (7, 10))

    def test_comida_so_em_espaco_livre(self):
        p = Partida()
        livre = (0, 0)
        p.obstaculos = {(x, y) for x in range(COLUNAS)
                        for y in range(LINHAS)} - set(p.cobra) - {livre}
        self.assertEqual(p.sortear_comida(), livre)

    def test_vitoria_sem_espacos_livres(self):
        p = Partida()
        p.comida = (9, 11)
        p.obstaculos = {(x, y) for x in range(COLUNAS)
                        for y in range(LINHAS)} - set(p.cobra) - {p.comida}
        p.avancar()
        self.assertTrue(p.fim)
        self.assertIsNone(p.comida)
        self.assertEqual(p.pontos, 1)
        self.assertIn('Vitória', p.mensagem)


if __name__ == '__main__':
    unittest.main()
