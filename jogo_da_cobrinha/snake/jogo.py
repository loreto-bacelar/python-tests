"""Interface gráfica, eventos de teclado e ciclo de atualização."""

from .configuracoes import CELULA, COLUNAS, DIRECOES, INTERVALO, LINHAS
from .partida import Partida


class Jogo:
    FUNDO = '#aac477'
    ESCURO = '#24351d'

    def __init__(self, raiz):
        import tkinter as tk
        self.raiz = raiz
        raiz.title('Snake Xenzia • Python')
        raiz.resizable(False, False)
        raiz.configure(bg=self.ESCURO)
        self.placar = tk.Label(raiz, font=('Courier', 17, 'bold'),
                               bg=self.ESCURO, fg=self.FUNDO, pady=14)
        self.placar.pack(fill='x')
        self.tela = tk.Canvas(raiz, width=COLUNAS * CELULA,
                              height=LINHAS * CELULA, bg=self.FUNDO,
                              highlightthickness=4, highlightbackground=self.ESCURO)
        self.tela.pack(padx=16)
        tk.Label(raiz, text='SETAS / WASD: mover    ESPAÇO: pausar    R: reiniciar    ESC: sair',
                 font=('Arial', 11), bg=self.ESCURO, fg=self.FUNDO, pady=14).pack()
        self.timer = None
        raiz.bind('<KeyPress>', self.tecla)
        raiz.protocol('WM_DELETE_WINDOW', self.fechar)
        self.reiniciar()

    def reiniciar(self):
        self.cancelar_timer()
        self.partida = Partida()
        self.iniciado = False
        self.pausado = False
        self.desenhar()

    def cancelar_timer(self):
        if self.timer is not None:
            self.raiz.after_cancel(self.timer)
            self.timer = None

    def tecla(self, evento):
        tecla = evento.keysym
        if len(tecla) == 1:
            tecla = tecla.lower()
        if tecla == 'Escape':
            self.fechar()
        elif tecla == 'r':
            self.reiniciar()
        elif not self.partida.fim:
            if tecla == 'space':
                if not self.iniciado:
                    self.iniciar()
                else:
                    self.pausado = not self.pausado
                    self.cancelar_timer()
                    if not self.pausado:
                        self.agendar()
                    self.desenhar()
            elif tecla in DIRECOES and not self.pausado:
                self.partida.mudar_direcao(DIRECOES[tecla])
                if not self.iniciado:
                    self.iniciar()

    def iniciar(self):
        self.iniciado = True
        self.desenhar()
        self.agendar()

    def agendar(self):
        self.timer = self.raiz.after(INTERVALO, self.atualizar)

    def atualizar(self):
        self.timer = None
        self.partida.avancar()
        self.desenhar()
        if not self.partida.fim:
            self.agendar()

    def desenhar(self):
        t, p = self.tela, self.partida
        t.delete('all')
        self.placar.config(text=f'SNAKE XENZIA    PONTOS: {p.pontos:03d}    TAMANHO: {len(p.cobra):03d}')
        for x, y in p.obstaculos:
            a, b = x * CELULA, y * CELULA
            t.create_rectangle(a+1, b+1, a+23, b+23, fill='#62734d', outline=self.ESCURO)
            t.create_line(a+5, b+5, a+19, b+19, fill=self.ESCURO)
            t.create_line(a+19, b+5, a+5, b+19, fill=self.ESCURO)
        if p.comida is not None:
            x, y = p.comida
            t.create_oval(x*CELULA+5, y*CELULA+5, x*CELULA+19, y*CELULA+19,
                          fill=self.ESCURO, outline=self.ESCURO)
        for i, (x, y) in enumerate(p.cobra):
            t.create_rectangle(x*CELULA+2, y*CELULA+2, x*CELULA+22, y*CELULA+22,
                               fill=self.ESCURO if i == 0 else '#40582d', outline=self.ESCURO)
        x, y = p.cobra[0]
        dx, dy = p.direcao
        for lado in (-1, 1):
            ex = x*CELULA+12 + dx*5 + (-dy)*lado*4
            ey = y*CELULA+12 + dy*5 + dx*lado*4
            t.create_oval(ex-2, ey-2, ex+2, ey+2, fill=self.FUNDO, outline='')
        if p.fim:
            self.aviso('VITÓRIA!' if p.comida is None else 'FIM DE JOGO',
                       p.mensagem + '\nPressione R para jogar novamente.')
        elif not self.iniciado:
            self.aviso('SNAKE XENZIA', 'Coma as bolinhas. Evite paredes, obstáculos e a cauda.\nPressione ESPAÇO ou uma seta para começar.')
        elif self.pausado:
            self.aviso('PAUSADO', 'Pressione ESPAÇO para continuar.')

    def aviso(self, titulo, texto):
        cx, cy = COLUNAS*CELULA/2, LINHAS*CELULA/2
        self.tela.create_rectangle(35, cy-76, COLUNAS*CELULA-35, cy+76,
                                   fill=self.ESCURO, outline=self.FUNDO, width=2)
        self.tela.create_text(cx, cy-30, text=titulo, fill=self.FUNDO,
                              font=('Courier', 25, 'bold'))
        self.tela.create_text(cx, cy+25, text=texto, fill=self.FUNDO,
                              font=('Arial', 13), justify='center', width=620)

    def fechar(self):
        self.cancelar_timer()
        self.raiz.destroy()

