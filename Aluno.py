# -*- coding: utf-8 -*-

class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

import tkinter as tk

def criar_janela():
    alunos = []
    janela = tk.Tk()
    janela.title("Cadastro de Aluno")

    frame = tk.Frame(janela)
    frame.pack()

    nome_label = tk.Label(frame, text="Nome:")
    nome_label.grid(row=0, column=0)
    nome_entry = tk.Entry(frame)
    nome_entry.grid(row=0, column=1)

    idade_label = tk.Label(frame, text="Idade:")
    idade_label.grid(row=1, column=0)
    idade_entry = tk.Entry(frame)
    idade_entry.grid(row=1, column=1)

    matricula_label = tk.Label(frame, text="Matrícula:")
    matricula_label.grid(row=2, column=0)
    matricula_entry = tk.Entry(frame)
    matricula_entry.grid(row=2, column=1)

    def criar_aluno():
        nome = nome_entry.get()
        idade = int(idade_entry.get())
        matricula = matricula_entry.get()
        aluno = Aluno(nome, idade, matricula)
        nome_entry.delete(0, tk.END)
        idade_entry.delete(0, tk.END)
        matricula_entry.delete(0, tk.END)
        alunos.append(aluno)
        
    criar_button = tk.Button(frame, text="Criar Aluno", command=criar_aluno)
    criar_button.grid(row=3, columnspan=2)
    mostrar_button = tk.Button(
        frame, text="Mostrar Alunos", command=lambda: mostrar_alunos(alunos))
    mostrar_button.grid(row=4, columnspan=2)
        
    janela.mainloop()

def mostrar_alunos(alunos):
    janela_alunos = tk.Toplevel()
    janela_alunos.title("Lista de Alunos")

    frame_alunos = tk.Frame(janela_alunos)
    frame_alunos.pack()

    for i, aluno in enumerate(alunos, start=1):
        label_aluno = tk.Label(frame_alunos, text=f"{i}. {aluno.nome}, {aluno.idade}, {aluno.matricula}")
        label_aluno.pack()


def criar_aluno(nome, idade, matricula):
    return Aluno(nome, idade, matricula)

criar_janela()