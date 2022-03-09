import pyautogui
import time

time.sleep(5) # Ao executar voce tem 5 segundos para posicionar o mouse sobre o botao desejado para capturar a posição

""" Atenção a minha resolução atual é 1080p ou seja 1920 x 1080
* A Captura da posição do mouse pode nao ser a mesma caso sua resolução seja diferente
* A Captura da posição do mouse pode nao ser a mesma em botoes do navegador 
caso seu zoom das paginas estiverem diferentes ex: com 100% de zoom sera uma posicão e com 120% a posição sera outra
"""
print(pyautogui.position())