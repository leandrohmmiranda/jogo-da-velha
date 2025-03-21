import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Jogo da Velha")
        self.turno = "X"
        self.tabuleiro = [[" "]*3 for _ in range(3)]
        self.botoes = [[None]*3 for _ in range(3)]

        self.criar_interface()
        self.janela.mainloop()

    def criar_interface(self):
        for i in range(3):
            for j in range(3):
                self.botoes[i][j] = tk.Button(self.janela, text=" ", font=("Arial", 20), width=5, height=2,
                                              command=lambda r=i, c=j: self.jogada(r, c))
                self.botoes[i][j].grid(row=i, column=j)

    def jogada(self, r, c):
        if self.tabuleiro[r][c] == " ":
            self.tabuleiro[r][c] = self.turno
            self.botoes[r][c].config(text=self.turno)
            if self.verificar_vencedor():
                messagebox.showinfo("Fim de jogo", f"Jogador {self.turno} venceu!")
                self.reiniciar_jogo()
            elif all(cell != " " for row in self.tabuleiro for cell in row):
                messagebox.showinfo("Fim de jogo", "Empate!")
                self.reiniciar_jogo()
            else:
                self.turno = "O" if self.turno == "X" else "X"

    def verificar_vencedor(self):
        for row in self.tabuleiro:
            if row[0] == row[1] == row[2] != " ":
                return True
        for col in range(3):
            if self.tabuleiro[0][col] == self.tabuleiro[1][col] == self.tabuleiro[2][col] != " ":
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != " ":
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != " ":
            return True
        return False

    def reiniciar_jogo(self):
        for i in range(3):
            for j in range(3):
                self.tabuleiro[i][j] = " "
                self.botoes[i][j].config(text=" ")
        self.turno = "X"

JogoDaVelha()
