"""Execute com: python main.py."""

from snake.jogo import Jogo


def main():
    try:
        import tkinter as tk
    except ImportError:
        raise SystemExit('Tkinter não está instalado. Instale o suporte Tk do seu Python.')
    try:
        raiz = tk.Tk()
    except tk.TclError as erro:
        raise SystemExit(f'Não foi possível abrir a janela. Execute em um ambiente gráfico.\n{erro}')
    Jogo(raiz)
    raiz.mainloop()


if __name__ == '__main__':
    main()
