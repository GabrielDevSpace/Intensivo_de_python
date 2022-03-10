""" Situaçõa: Importadora de Produtos
Preciso capturar dados de valores dolar ouro euro automaticamente da web
para isso usaremos o selenium, controla nosso navegador de forma automatica,
sem a necessidade de parar a maquina para o processo rodar.
# Requisitos Selenium e webdriver = (Chromedriver.exe, Geckodriver.exe)
# webdriver download e colocar dentro da pasta de instalação do python PATH c:/User/AppData/Local/Programs/Python
"""

from selenium import webdriver  # Controlar navegador
from selenium.webdriver.common.keys import Keys  # Usar Teclado
from selenium.webdriver.common.by import By  # Localizar itens no navegador
import pandas as pd
import webbrowser


# Configuração necessaria para acessar Chrome Oculto
options = webdriver.ChromeOptions()
options.add_argument("--headless")

# Abrir o Browser do Chrome
navegador = webdriver.Chrome(options=options)


# Instruir navegador a acessar um site
navegador.get("https://www.google.com.br/")

# Encontrando elementos como barra de pesquisar botoes etc
# Usando o inspecionar do Chrome encontre o campo que deseja, Click botao direito Copy > Copy.XPath
# Posso referenciar por XPath, Id, Name, Class ... etc

# Digitando na barra de pesquisa
# Pressionando no Botão Enter para pesquisar
navegador.find_element(By.XPATH,
                       "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("cotação dolar",
                                                                                                        Keys.ENTER)

# Pegando o value do elemento do campo e adicionando em uma variavel
cotacao_dollar = navegador.find_element(
    By.XPATH, "//*[@id='knowledge-currency__updatable-data-column']/div[1]/div[2]/span[1]").get_attribute('data-value')

# Cotação Bitcoin
navegador.get("https://coinmarketcap.com/currencies/bitcoin/")

cotacao_btc = navegador.find_element(
    By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span') \
    .get_attribute('innerHTML')

# Tratando o formato para realizar calculos, retirando mais de um caracter da string $ e ,
b = {',': '', '$': ''}
for x, z in b.items():
    cotacao_btc = cotacao_btc.replace(x, z)

# Realizando o Calculo do BTC em dollar * valor dolarBRL
cotacao_btc = float(cotacao_btc)
cotacao_dollar = float(cotacao_dollar)
cotacao_dollar = float("{:.2f}".format(cotacao_dollar))
cotacao_btc_real = float("{:.2f}".format(cotacao_dollar * cotacao_btc))

print(f"Dolar: {cotacao_dollar}\nBitcoin: {cotacao_btc_real} ")

navegador.quit()

# Realizando a importação e atualização da nossa tabela de dados
tabela = pd.read_excel("Produtos.xlsx")

# Atualizar campos de cotação do dollar na planilha
# localizar o que o python ira alterar tabela.loc[linha, coluna] = float(valor_a_ser_gravado)
# Linha sera igual todos os valores dólar na coluna MOEDA
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dollar)
tabela.loc[tabela["Moeda"] == "Bitcoin", "Cotação"] = float(cotacao_btc_real)

# Realizando os calculos
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

tabela.to_excel("ProdutosAtualizados.xlsx", index=False)  # Nao exportar o Index

html = tabela.to_html(index=False)  # Nao Exportar o Index
text_file = open("ResultadoGeral.html", "w")
text_file.write(html)
text_file.close()
webbrowser.open('ResultadoGeral.html')

