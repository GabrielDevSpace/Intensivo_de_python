import pandas as pd
import webbrowser

# (r"local_file") com o R estaremos ignorando os caracteres especiais
# para o py nao confundir C:\navio com \n que é quebra de linha

tabela = pd.read_excel(r"C:\Users\USUARIO\Downloads\populacao-e-pib-por-estados.xlsx")

populacao_total = tabela["População"].sum() / 2
pib_total = tabela["PIB"].sum() / 2

print(f"""População e PIB do BRASIL extraidos com pandas de um .xlsx 
baixado por uma rotina automatica com pyautogui\n\nPopulação: {populacao_total:,.0f}\nPIB: R$ {pib_total:,.2f}""")

pd.options.display.float_format = '{:,.0f}'.format

# Salvando Resultados em um HTML
html = tabela.to_html()
text_file = open("ResultadoGeral.html", "w")
text_file.write(html)
text_file.close()

# Exibir no browser o arquivo HTML gerado
webbrowser.open('ResultadoGeral.html')
