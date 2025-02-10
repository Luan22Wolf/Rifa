import random
import tkinter as tk
from tkinter import ttk, messagebox
import threading

# Dicionário para armazenar nomes e números escolhidos
rifa = {}

# Função para adicionar participante
def adicionar_participante():
    nome = nome_entry.get().strip()
    numeros = numeros_entry.get().strip().split()
    
    # Validação do nome
    if not nome.isalpha():
        messagebox.showerror("Erro", "O nome deve conter apenas letras.")
        return
    nome = nome.title()  # Capitaliza a primeira letra
    
    # Validação dos números
    try:
        numeros = [int(n) for n in numeros]
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números separados por espaço.")
        return

    # Verifica números já escolhidos
    numeros_disponiveis = set(range(1, 101)) - {n for lista in rifa.values() for n in lista}
    numeros_validos = [n for n in numeros if n in numeros_disponiveis]
    
    if not numeros_validos:
        messagebox.showwarning("Aviso", "Todos os números já foram escolhidos. Tente novamente.")
        return

    rifa[nome] = numeros_validos
    atualizar_lista()
    nome_entry.delete(0, tk.END)
    numeros_entry.delete(0, tk.END)

# Função para sortear um número
def sortear_numero():
    if not rifa:
        messagebox.showwarning("Aviso", "Nenhum participante foi adicionado.")
        return
    
    for i in range(5, 0, -1):
        contador_label.config(text=f"Sorteando em {i} segundos...")
        janela.update()
        janela.after(1000)

    numero_sorteado = random.randint(1, 100)
    vencedores = [nome for nome, numeros in rifa.items() if numero_sorteado in numeros]
    resultado_label.config(
        text=f"Número sorteado: {numero_sorteado}\nVencedor(es): {', '.join(vencedores) if vencedores else 'Nenhum'}"
    )

# Função para atualizar a lista de participantes
def atualizar_lista():
    lista_participantes.delete(*lista_participantes.get_children())
    for nome, numeros in rifa.items():
        lista_participantes.insert("", "end", values=(nome, ", ".join(map(str, numeros))))

# Configurar a interface gráfica
janela = tk.Tk()
janela.title("Rifa - Sorteio")
janela.geometry("600x500")

# Criar estilos
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("TLabel", font=("Arial", 14))

# Nome
ttk.Label(janela, text="Nome do Participante:").pack(pady=5)
nome_entry = ttk.Entry(janela)
nome_entry.pack(pady=5)

# Números
ttk.Label(janela, text="Números escolhidos (separados por espaço):").pack(pady=5)
numeros_entry = ttk.Entry(janela)
numeros_entry.pack(pady=5)

# Botões
ttk.Button(janela, text="Adicionar Participante", command=adicionar_participante).pack(pady=5)
ttk.Button(janela, text="Sortear Número", command=lambda: threading.Thread(target=sortear_numero).start()).pack(pady=5)
ttk.Button(janela, text="Sair", command=janela.quit).pack(pady=5)

# Exibir contagem regressiva e resultado
contador_label = ttk.Label(janela, text="")
contador_label.pack(pady=5)
resultado_label = ttk.Label(janela, text="Resultado aparecerá aqui", font=("Arial", 16))
resultado_label.pack(pady=5)

# Lista de participantes
lista_participantes = ttk.Treeview(janela, columns=("Nome", "Números"), show="headings")
lista_participantes.heading("Nome", text="Nome")
lista_participantes.heading("Números", text="Números Escolhidos")
lista_participantes.pack(pady=5, fill="both", expand=True)

janela.mainloop()