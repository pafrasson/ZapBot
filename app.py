import customtkinter as tk
from customtkinter import *
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
from tkinter import scrolledtext
import sys
from io import StringIO
from selenium import webdriver

window = tk.CTk()
window.geometry("500x500")
window.title("ZapBot by Frass")
window.iconbitmap('./assets/mainicon.ico')

class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_space = text_widget

    def write(self, message):
        self.text_space.insert(tk.END, message)
        self.text_space.see(tk.END)  # Rola automaticamente para a última linha
        
def connect_wpp():
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    
def selecionar_arquivo():
    selected_archive = filedialog.askopenfilename()

    if selected_archive:
        global gbl_selected_arquive
        gbl_selected_arquive = selected_archive
        print("Caminho do arquivo selecionado:", gbl_selected_arquive)
    else:
        print("Nenhum arquivo selecionado")
        
def custom_msg():
    nova_janela = tk.CTkToplevel(window)
    nova_janela.geometry("300x300")
    nova_janela.title("Personalizar mensagem")
    msg_label = tk.CTkTextbox(nova_janela, width=200, height=200, wrap="word")
    msg_label.pack(padx=30,pady=30)
    
    def save():
        global texto_global
        texto_global = msg_label.get("1.0", tk.END)
        print("texto salvo com sucesso")
        
    btn_save = tk.CTkButton(nova_janela, text="Salvar", command=save).pack(padx=10, pady=10)

def iniciar_envio():
    txt = gbl_selected_arquive
    arquivo = open(txt, "r")
    for linha in arquivo.readlines():
        if linha == "":
            break
        print(f'mensagem enviada para{linha}')
        msg = texto_global

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

Button_connectwpp = CTkButton(
    master= window,
    command=connect_wpp,
    text= "Conectar Whatsapp",
    text_color="#79ae61",
    hover= True,
    hover_color= "black",
    height=30,
    width= 80,
    border_width=2,
    corner_radius=3,
    border_color= "#79ae61", 
    bg_color="#262626",
    fg_color= "#262626").pack(padx=0, pady=5)

hellotext = tk.CTkLabel(window, text="Bem vindo!", font=("Arial", 16, "bold")).pack(padx=10, pady=50)

btn_select_arquive = tk.CTkButton(window, text="Importar lista de contatos", command=selecionar_arquivo).pack(padx=10, pady=10)

btn_custom_msg = tk.CTkButton(window, text="Mensagem de envio", command=custom_msg).pack(padx=10, pady=10)

btn_send_msg = tk.CTkButton(window, text="Iniciar envio", bg_color="#262626", command=iniciar_envio).pack(padx=10, pady=10)

text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
text_area.pack(padx=10, pady=50)
sys.stdout = StdoutRedirector(text_area)

window.mainloop()