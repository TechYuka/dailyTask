# Cria uma janela que me passa uma "missão" quando eu finalizar essa missão clico em feito o que fecha a janela
# Ao clicar em feito o botão envia para o arquivo txt linha o dado que passa para proxima tarefa (quando o arquivo c++ abrir o janela na proxima inicialização do sistema)

import customtkinter as ctk # Importando a biblioteca para GUI

# Função para fechar a janela
def fechar_janela():
    janela.destroy()  # Fecha a janela

# Função do botão
def button_event():
    width
    with open("linha.txt", "r+") as arquivo:  # Atualiza o programa para passar para a próxima task
        linha = arquivo.read()
        arquivo.seek(0)
        arquivo.write(str(int(linha) + 1))  # Incrementa a linha no arquivo

    with open("listaTasks.txt", "a") as arquivo: # Só para ter um "log" de conclusão
        arquivo.write("\n" + str(int(linha)))
    
    janela.destroy()

with open("task.txt", "r") as arquivo:  # Aqui o programa carrega a task
    conteudo = arquivo.read()

# Cria janela
janela = ctk.CTk()


# Configurando a janela principal
janela.title("Daily task")
janela.geometry("300x300")
janela.resizable(width=False, height=False)  # Não permite o usuário mudar o tamanho da janela
janela.attributes("-topmost", True) # Mantém a janela sempre sobreposta
screen_width = janela.winfo_screenwidth() # Calcula a largura da tela principal
second_screen_x = -screen_width  # Posiciona na largura total da tela principal
second_screen_y = 0  # No topo da tela
janela.geometry(f"300x300+{second_screen_x}+{second_screen_y}")  # Ajusta para a segunda tela

# Configurando o evento de fechar a janela com o botão "X"
janela.protocol("WM_DELETE_WINDOW", fechar_janela)

# Conteúdo da janela
textbox = ctk.CTkTextbox(janela, width=300, height=250)
textbox.pack(pady=5, padx=5)
textbox.insert("0.0", "Olá meu caro,\nTenha um dia maravilhoso!\n\nSua missão de hoje está neste link:\n\n" + "\t" + conteudo + "\n\n\tBoa sorte!")
textbox.configure(state="disabled")  # Configure textbox como somente leitura

# Botão 
botao = ctk.CTkButton(janela, text="Feito!", command=button_event, fg_color="black", hover_color="red", text_color="white")
botao.pack(side=ctk.RIGHT, padx=5, pady=5)  # Adiciona o botão

# Inicializa a janela
janela.mainloop()
