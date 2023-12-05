import customtkinter as tk
from customtkinter import *
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui

window = tk.CTk()
window.geometry("500x400")
window.title("ZapBot by Frass")


def selecionar_arquivo():
    selected_archive = filedialog.askopenfilename()

    if selected_archive:
        global gbl_selected_arquive
        gbl_selected_arquive = selected_archive
        print("Caminho do arquivo selecionado:", gbl_selected_arquive)
    else:
        print("Nenhum arquivo selecionado")
        
def custom_msg():
    pass

def iniciar_envio():
    txt = gbl_selected_arquive
    arquivo = open(txt, "r")
    for linha in arquivo.readlines():
        if linha == "":
            break
        print(linha)
        msg = f'Otimize Seu Negócio de Materiais de Construção com a Astersoft 🚀Olá, sou o Pedro da Astersoft! Nosso sistema é perfeito para gerenciar pedidos, entregas futuras e notas fiscais em seu comércio de materiais de construção. Assista ao vídeo rápido para ver como podemos facilitar a sua vida:'

        try:
            link_wpp = f'https://web.whatsapp.com/send?phone={
                linha}&text={quote(msg)}'
            webbrowser.open(link_wpp)
            sleep(20)
            seta = pyautogui.locateCenterOnScreen('send_btn.png')
            sleep(5)
            pyautogui.click(seta[0], seta[1])
            sleep(5)
            pyautogui.hotkey('ctrl' + 'w')
        except:
            print(f'nao foi possivel enviar mensagem para {linha}')
            with open('erros.txt', 'a', newline='', encoding='utf-8') as arquivo:
                arquivo.write(f'{linha}')


hellotext = tk.CTkLabel(window, text="Bem vindo!").pack(padx=10, pady=10)

btn_select_arquive = tk.CTkButton(window, text="Importar lista de contatos", command=selecionar_arquivo).pack(padx=10, pady=10)

btn_custom_msg = tk.CTkButton(window, text="Mensagem de envio", command=custom_msg).pack(padx=10, pady=10)

btn_send_msg = tk.CTkButton(window, text="Iniciar envio", command=iniciar_envio).pack(padx=10, pady=10)

window.mainloop()