import random
import tkinter as tk
from tkinter import messagebox
import time
import threading

# Dicionário para armazenar nomes e números escolhidos
rifa = {}

# Variável para armazenar o número sorteado
numero_sorteado = None

# Função para adicionar nomes e números escolhidos
def adicionar_participante():
    nome = nome_entry.get()
    numeros = numeros_entry.get().split()
    numeros = [int(numero) for numero in numeros]
    rifa[nome] = numeros
    resultado_label.config(text=f"{nome} escolheu os números {', '.join(map(str, numeros))}.")

# Função para realizar o sorteio e mostrar o resultado
def sortear_numero():
    global numero_sorteado
    contador_label.config(text="Contagem regressiva: 10")
    for i in range(10, 0, -1):
        contador_label.config(text=f"Contagem regressiva: {i}")
        time.sleep(1)
    numero_sorteado = random.randint(1, 100)
    nomes_vencedores = [nome for nome, numeros in rifa.items() if numero_sorteado in numeros]
    if nomes_vencedores:
        resultado = f"Número sorteado: {numero_sorteado}\nNome(s) do(s) vencedor(es): {', '.join(nomes_vencedores)}"
    else:
        resultado = f"Número sorteado: {numero_sorteado}\nNenhuma pessoa escolheu este número."
    resultado_label.config(text=resultado)

# Configurar a janela principal
janela = tk.Tk()
janela.title("RIFA PERFUME MASCULINO OU FEMININO")

# Alterar o fundo para azul
janela.configure(bg="gray")

# Rótulos e campos de entrada com cor de texto branca
nome_label = tk.Label(janela, text="NOME DOS PARTICIPANTES:", fg="black", bg="white")
nome_label.config(font=("Arial", 24))  # Define o tamanho da fonte para 16 pontos
nome_label.pack()

nome_entry = tk.Entry(janela)
nome_entry.pack()

numeros_label = tk.Label(janela, text="Números escolhidos (separados por espaço):", fg="purple", bg="white")
numeros_label.config(font=("Arial", 24))  # Define o tamanho da fonte para 16 pontos
numeros_label.pack()

numeros_entry = tk.Entry(janela)
numeros_entry.pack()

contador_label = tk.Label(janela, text="", fg="red", bg="gray")
contador_label.config(font=("Arial", 24))  # Define o tamanho da fonte para 16 pontos
contador_label.pack()

resultado_label = tk.Label(janela, text="AQUI VAI APARECER O UM NÚMERO ALEATÓRIO DE 1 ATÉ 100", fg="black", bg="white")
resultado_label.config(font=("Arial", 24))  # Define o tamanho da fonte para 16 pontos
resultado_label.pack()

# Botões com cor de texto preta
adicionar_botao = tk.Button(janela, text="ADICIONAR PARTICIPANTES", command=adicionar_participante, fg="purple")
adicionar_botao.config(width=24, height=4)  # Define a largura para 20 caracteres e a altura para 2 linhas
adicionar_botao.pack()

sortear_botao = tk.Button(janela, text="SORTEAR NÚMERO", command=lambda: threading.Thread(target=sortear_numero).start(), fg="green")
sortear_botao.config(width=24, height=4)  # Define a largura para 20 caracteres e a altura para 2 linhas
sortear_botao.pack()

sair_botao = tk.Button(janela, text="SAIR", command=janela.quit, fg="red")
sair_botao.config(width=24, height=4)  # Define a largura para 20 caracteres e a altura para 2 linhas
sair_botao.pack()

# Definir o tamanho da janela
janela.geometry("800x600")

# Iniciar a interface gráfica
janela.mainloop()