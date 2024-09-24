import customtkinter as ctk  # Importando a biblioteca para GUI
import json
import os
import sys

# Função para encontrar o caminho correto do arquivo
def resource_path(relative_path):
    """Obtenha o caminho absoluto para o arquivo 'dados.json', seja no desenvolvimento ou no executável."""
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

# Carrega os dados do json
def carregar_lista():  # Lista de tasks
    try: 
        # Usando resource_path para garantir que o caminho está correto
        with open(resource_path('dados.json'), 'r') as arquivo:
            lista = json.load(arquivo)
            return lista['lista']  # Retorna lista
            
    except (FileNotFoundError, KeyError):
        return []  # Retorna a frase erro
        
def salvar_lista(lista, primeira_linha):
    primeira_linha = lista.pop(0)
    lista.append(primeira_linha)  # Adiciona a primeira linha a lista
    # Usando resource_path para garantir o caminho correto
    with open(resource_path('dados.json'), 'w') as arquivo:
        json.dump({"lista": lista}, arquivo, indent=4)  # Salva a lista editada
        
def lista_para_linha(lista):
    lista = carregar_lista()
    if lista:  # Verifica se lista não está vazia
        primeira_linha = lista.pop(0)
        return primeira_linha
    else:
        return "Erro na função carregar_lista(): lista vazia."  # Retorna uma mensagem de erro
        
# Personalização da janela

def fechar_janela():  # Função para fechar a janela
    janela.destroy()
    
def button_event(lista, primeira_linha):
    salvar_lista(lista, primeira_linha)
    fechar_janela()

# Janela do app
janela = ctk.CTk()  # Cria a janela
janela.title("Daily task")  # Define o título da janela
janela.geometry("300x300")  # Define o tamanho da janela 
janela.resizable(width=False, height=False)  # Define o tamanho da janela como imutável
janela.attributes("-topmost", True)  # Outros apps não podem sobrepor a janela
screen_width = janela.winfo_screenwidth()  # Largura da tela
second_screen_x = -screen_width  # Define o x da segunda tela negativando a largura da primeira
second_screen_y = 0
janela.geometry(f"300x300+{second_screen_x}+{second_screen_y}")  # Define a janela para abrir no canto mais à esquerda
janela.protocol("WM_DELETE_WINDOW", fechar_janela)  # Configurando o evento de fechar a janela com o botão "X"

# Começa a trabalhar com o arquivo json
lista = carregar_lista()  # "Baixa" a lista para o programa
primeira_linha = lista_para_linha(lista)

# Define um text box
textbox = ctk.CTkTextbox(janela, width=300, height=250)
textbox.pack(pady=5, padx=5)
textbox.insert("0.0", "Olá meu caro,\nTenha um dia maravilhoso!\n\nSua missão de hoje está neste link:\n\n" + "\t" + primeira_linha + "\n\n\tBoa sorte!")
textbox.configure(state="disabled")  # Configura o textbox como somente leitura
    
# Botão 
botao = ctk.CTkButton(janela, text="Feito!", command=lambda: button_event(lista, primeira_linha), fg_color="black", hover_color="red", text_color="white")
botao.pack(side=ctk.RIGHT, padx=5, pady=5)  # Adiciona o botão

# Inicializa a janela
janela.mainloop()
