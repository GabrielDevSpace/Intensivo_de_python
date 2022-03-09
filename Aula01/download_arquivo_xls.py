import pyautogui
import pyperclip

# Biblioteca para controlar o tempo de pausa para o programa nao se perder caso a pagina demore para carregar
import time

"""
Com essas bibliotecas podemos controlar nosso teclado e mouse
Tarefas cotidianas e repetitivas que sempre seguem um padrao podem ser automatizadas
Envio de emails, extração de relatorios de um segundo sistema, navegação em telas
"""

# Passos para abrir o navegador Chrome no windows
pyautogui.press("Win")  # Apertando apenas uma tecla
pyautogui.write("chrome")  # Escrevendo
pyautogui.press("Enter")  # Apertando um conjunto de teclas

# Passos para abrir uma nova aba
pyautogui.hotkey("Ctrl","t")
time.sleep(2)

# O pyautogui nao lida bem com caracteres especiais como ?, * para isso usamos o pyperclip
# que apenas copia um texto pronto e nao precisa digita-lo como se fosse o write do pyautogui
pyperclip.copy("http://www.servicos.blog.br/wp-content/uploads/2013/10/populacao-e-pib-por-estados.xlsx")
pyautogui.hotkey("Ctrl","v")
time.sleep(2)
pyautogui.press("Enter")

# Passos para clicar no botão de download do arquivo
# time.sleep(5)
# pyautogui.click(x=949, y=398, button='right')

time.sleep(5)
pyautogui.hotkey("Alt","F4")