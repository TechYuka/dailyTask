# Programa completo em python3

import customtkinter as ctk # Importando a biblioteca para GUI

import json

# Carrega os dados do json
def carregar_lista(): # Lista de tasks
    try: 
        with open('dados.json', 'r') as arquivo:
            lista =json.load(arquivo)
            return lista['lista'] # Retorna lista
            
    except (FileNotFoundError, KeyError):
        return [] # Retorna a frase erro
        
def salvar_lista(lista, primeira_linha):
    primeira_linha = lista.pop(0)
    lista.append(primeira_linha) # Adiciona a primeira linha a lista
    with open('dados.json', 'w') as arquivo:
        json.dump({"lista": lista}, arquivo, indent=4) # Salva a lista editada
        
def lista_para_linha(lista):
    lista = carregar_lista()
    if lista: # Verifica se lista não está vazia
        primeira_linha = lista.pop(0)
        return primeira_linha
    else:
        return "Erro na função carregar_lista(): lista vazia."  # Retorna uma mensagem de erro
        
# Personalização da janela

def fechar_janela(): # Função para fechar a janela
    janela.destroy()
    
def button_event(lista, primeira_linha):
    salvar_lista(lista, primeira_linha)
    fechar_janela()
    

janela = ctk.CTk() # Cria a janela
janela.title("Daily task") # Define o titulo da janela
janela.geometry("300x300") # Define o tamanha da janela 
janela.resizable(width=False, height=False) # Define o tamanho da janela como imutável
janela.attributes("-topmost", True) # Outros apps não podem sobrepor a janela
screen_width = janela.winfo_screenwidth() # Define a largura total da janela que abriu o app
second_screen_x = -screen_width # Define o x da segunda tela negativando a largura da primeira
second_screen_y = 0
janela.geometry(f"300x300+{second_screen_x}+{second_screen_y}") # Define a janela para abrir no canto mais a esquerda possivel contando com a 2 tela
janela.protocol("WM_DELETE_WINDOW", fechar_janela) # Configurando o evento de fechar a janela com o botão "X" / Chama a função fechar_janela

# Começa a trabalhar com o arquivo json
lista = carregar_lista() # "Baixa" a lista para o programa
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




