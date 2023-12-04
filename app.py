from urllib.parse import quote
import webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/')
sleep(30)

arquivo = open("arquivo.txt", "r")
for linha in arquivo.readlines():
    if linha == "":
        break
    print(linha)

    msg = f'Otimize Seu Negócio de Materiais de Construção com a Astersoft 🚀Olá, sou o Pedro da Astersoft! Nosso sistema é perfeito para gerenciar pedidos, entregas futuras e notas fiscais em seu comércio de materiais de construção. Assista ao vídeo rápido para ver como podemos facilitar a sua vida:'
    link_wpp = f'https://web.whatsapp.com/send?phone={linha}&text={quote(msg)}'
    webbrowser.open(link_wpp)
