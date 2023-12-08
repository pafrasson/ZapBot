import customtkinter as tk
from customtkinter import *
from urllib.parse import quote
import webbrowser
from time import sleep
from tkinter import scrolledtext
import sys
from io import StringIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

service = Service(ChromeDriverManager().install())

def start():
    nav2 = webdriver.Chrome(service=service)
    global nav
    nav = nav2

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
    nav.get('https://web.whatsapp.com')

def selecionar_arquivo():
    selected_archive = filedialog.askopenfilename()

    if selected_archive:
        global gbl_selected_arquive
        gbl_selected_arquive = selected_archive
        print("Caminho do arquivo selecionado:", gbl_selected_arquive)
    else:
        print("Nenhum arquivo selecionado")

def selecionar_midia():
    selected_archive = filedialog.askopenfilename()

    if selected_archive:
        global gbl_selected_media
        gbl_selected_media = selected_archive
        print("Caminho da mídia selecionado:", gbl_selected_media)
    else:
        print("Nenhuma mídia selecionado")

def custom_msg():
    nova_janela = tk.CTkToplevel(window)
    nova_janela.geometry("300x300")
    nova_janela.title("Personalizar mensagem")
    msg_label = tk.CTkTextbox(nova_janela, width=200, height=200, wrap="word")
    msg_label.pack(padx=30, pady=30)

    def save():
        global texto_global
        texto_global = msg_label.get("1.0", tk.END)
        print("texto salvo com sucesso")

    btn_save = tk.CTkButton(nova_janela, text="Salvar",
                            command=save).pack(padx=10, pady=10)

def iniciar_envio():
    txt = gbl_selected_arquive
    msg = texto_global
    media = gbl_selected_media
    with open(txt, 'r') as arquivo:

        for linha in arquivo.readlines():
            if linha == "":
                break
            print(f'enviando mensagem para {linha}')

            try:
                nav.get(
                    f'https://web.whatsapp.com/send?phone={linha}&text={quote(msg)}')
                sleep(5)
                print(f'Current URL: {nav.current_url}')
                 
                wait = WebDriverWait(nav, 10)
                button_locator = (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
                button = wait.until(EC.element_to_be_clickable(button_locator))
                button.click()
                sleep(5)
                
                if media:
                    clip_icon_locator = (By.CSS_SELECTOR, 'div[data-testid="clip"]')
                    clip_icon = WebDriverWait(nav, 10).until(EC.element_to_be_clickable(clip_icon_locator))
                    clip_icon.click()

                    media_option_locator = (By.CSS_SELECTOR, 'input[type="file"]')
                    media_option = WebDriverWait(nav, 10).until(EC.element_to_be_clickable(media_option_locator))
                    media_option.send_keys(media)
                    
                    button = wait.until(EC.element_to_be_clickable(button_locator))
                    button.click()
                    sleep(5)
            except NoSuchElementException as e:
                print(f'Error finding element: {e}')
            except TimeoutException as e:
                print(f'Timeout waiting for element: {e}')
            except Exception as e:
                print(f'Unexpected error: {e}')
                with open('erros.txt', 'a', newline='', encoding='utf-8') as arquivo:
                    arquivo.write(f'{linha}')

frame2 = CTkFrame(window)
frame2.pack(expand=True, anchor=NW, padx=10, pady=10)

button_image = CTkImage(
    Image.open('assets/start.png').resize((20, 20)))
Button_start = tk.CTkButton(
    master=frame2,
    image=button_image,
    text="",
    command=start,
    hover=True,
    hover_color="gray",
    height=30,
    width=30,
    border_width=2,
    corner_radius=3,
    border_color="black",
    compound=LEFT,
    fg_color="#262626")

Button_start.pack(padx=0, pady=5)

buttonwpp_image = CTkImage(
    Image.open('assets/whatsapp.png').resize((20, 20)))

Button_connectwpp = tk.CTkButton(
    master=frame2,
    command=connect_wpp,
    image=buttonwpp_image,
    text="",
    text_color="#79ae61",
    hover=True,
    hover_color="black",
    height=30,
    width=30,
    border_width=2,
    corner_radius=3,
    border_color="#79ae61",
    bg_color="#262626",
    compound=LEFT,
    fg_color="#262626")
Button_connectwpp.pack(anchor=S, expand=True, padx=0, pady=5)

hellotext = tk.CTkLabel(window, text="ZapBot", font=("Arial", 24, "bold"))
hellotext.pack(expand=True, padx=5, pady=10)

frame = CTkFrame(window, border_width=0)
frame.pack(expand=True)

btn_select_arquive = tk.CTkButton(
    frame, text="Importar lista de contatos", command=selecionar_arquivo)
btn_select_arquive.pack(anchor=S, expand=True, padx=5, pady=10)

btn_custom_msg = tk.CTkButton(
    frame, text="Mensagem de envio", command=custom_msg)
btn_custom_msg.pack(anchor=S, expand=True, padx=5, pady=10)

btn_select_media = tk.CTkButton(
    frame, text="Selecionar Mídia", command=selecionar_midia)
btn_select_media.pack(anchor=S, expand=True, padx=5, pady=10)

btn_send_msg = tk.CTkButton(
    frame, text="Iniciar envio", bg_color="#262626", command=iniciar_envio)
btn_send_msg.pack(anchor=N, expand=True, padx=5, pady=10)

text_area = scrolledtext.ScrolledText(
    window, wrap=tk.WORD, width=40, height=10)
text_area.pack(expand=True, padx=5, pady=10)
sys.stdout = StdoutRedirector(text_area)

window.mainloop()