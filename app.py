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

frame2 = CTkFrame(window)
frame2.pack(expand=True, anchor = NW, padx=5, pady=10)
Button_connectwpp = tk.CTkButton(
    master= frame2,
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
    compound=LEFT,
    fg_color= "#262626")
Button_connectwpp.pack(anchor = S, expand=True, padx=0, pady=0)

hellotext = tk.CTkLabel(window, text="ZapBot", font=("Arial", 24, "bold"))
hellotext.pack(expand=True, padx=5, pady=10)

frame = CTkFrame(window, border_width=0)
frame.pack(expand=True)

btn_select_arquive = tk.CTkButton(frame, text="Importar lista de contatos", command=selecionar_arquivo)
btn_select_arquive.pack(anchor = S, expand=True, padx=5, pady=10)

btn_custom_msg = tk.CTkButton(frame, text="Mensagem de envio", command=custom_msg)
btn_custom_msg.pack(anchor = S, expand=True, padx=5, pady=10)

btn_send_msg = tk.CTkButton(frame, text="Iniciar envio", bg_color="#262626", command=iniciar_envio)
btn_send_msg.pack(anchor = N, expand=True, padx=5, pady=10)

text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
text_area.pack(expand=True, padx=5, pady=10)
sys.stdout = StdoutRedirector(text_area)

window.mainloop()