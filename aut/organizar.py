import os
import shutil
import tkinter as tk
from tkinter import filedialog

def organizar_arquivos(origem, destino):
    # Verifica se o diretório de destino existe, se não, cria
    if not os.path.exists(destino):
        os.makedirs(destino)

    for filename in os.listdir(origem):
        # Modifique as condições de classificação conforme necessário
        if filename.endswith(".pdf"):
            categoria = "Documentos PDF"
        elif filename.endswith(".txt"):
            categoria = "Documentos de Texto"
        else:
            categoria = "Outros"

        # Caminho de origem e destino para o arquivo
        origem_arquivo = os.path.join(origem, filename)
        destino_categoria = os.path.join(destino, categoria)

        # Cria o diretório de categoria se não existir
        if not os.path.exists(destino_categoria):
            os.makedirs(destino_categoria)

        # Move o arquivo para a pasta de destino
        shutil.move(origem_arquivo, os.path.join(destino_categoria, filename))

def selecionar_diretorio(tipo):
    diretorio = filedialog.askdirectory(title=f"Selecione o diretório de {tipo}")
    if tipo == "origem":
        entry_origem.delete(0, tk.END)
        entry_origem.insert(0, diretorio)
    else:
        entry_destino.delete(0, tk.END)
        entry_destino.insert(0, diretorio)

def executar_automacao():
    diretorio_origem = entry_origem.get()
    diretorio_destino = entry_destino.get()
    organizar_arquivos(diretorio_origem, diretorio_destino)

# Criação da Interface Gráfica
app = tk.Tk()
app.title("Organizador de Arquivos")

# Entradas de Texto
tk.Label(app, text="Diretório de Origem:").pack()
entry_origem = tk.Entry(app, width=50)
entry_origem.pack()
tk.Button(app, text="Selecionar Origem", command=lambda: selecionar_diretorio("origem")).pack()

tk.Label(app, text="Diretório de Destino:").pack()
entry_destino = tk.Entry(app, width=50)
entry_destino.pack()
tk.Button(app, text="Selecionar Destino", command=lambda: selecionar_diretorio("destino")).pack()

# Botão de Execução
tk.Button(app, text="Executar Automação", command=executar_automacao).pack()

# Execução da Interface Gráfica
app.mainloop()




#abaixo eu coloquei um modelo para teste padrão na IDE
#if __name__ == "__main__":
    # Diretório de origem (onde estão os arquivos a serem organizados)
    #diretorio_origem = "Caminho\\Para\\Sua\\Pasta\\Origem"

    # Diretório de destino (onde os arquivos serão organizados)
    #diretorio_destino = "Caminho\\Para\\Sua\\Pasta\\Destino"

    #organizar_arquivos(diretorio_origem, diretorio_destino)
