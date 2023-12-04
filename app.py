from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui

arquivo = open("arquivo.txt", "r")
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
