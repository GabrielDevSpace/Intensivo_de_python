import pandas as pd
import plotly.express as px
import webbrowser
"""
Cenario: Empresa de telecom com Cancelamentos Recorrentes
Clientes de varios serviços Diferentes como INTERNET  e TELEFONE
O problema: Analisando o historico dos clientes dos ultimos anos voce percebe 
que a empresa esta com churn de >26%  ou seja cancelamentos.
Perdas de milhoes para a empresa.
O que a empresa precisa fazer para resolver isso?
"""

# Importar as bases de dados dos clientes
tabela = pd.read_csv("telecom_users.csv")

# Entender as Informações disponiveis
# Entender os erros a modelagem necessaria da base de dados - Tratamento de Dados
tabela = tabela.drop(["Unnamed: 0","IDCliente"], axis=1)  # Axis=0 - Linha  Axis=1 - Coluna

# Analisar se o python esta lendo os tipos de dados corretamente, numeros estao como int float ou apenas strings?
print(tabela.info())  # ira exibir as informações de cada coluna se esta no tipo correto, campos em branco, etc.
# Ao identificar uma coluna com tipo diferente terei de transformar o tipo da coluna
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# Existe alguma linha vazias ou campo vazio? isso poderia afetar as comparações
tabela = tabela.dropna(how="all", axis=1)  # Exclui todas colunas completamente vazias
tabela = tabela.dropna(how="any", axis=0)  # Exclui todas as linhas com 1 ou mais colunas vazias
# how=all exclui quando completamente vazia, how=any pelo menos 1 informação vazia

# Analise Macro
# Quantos clientes cancelaram e quantos estao ativos
print(tabela["Churn"].value_counts()) # Ativos = 4387 / Cancelados = 1587

# % clientes cancelaram x % Cliente ativos
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format)) # Ativos = 73% / Cancelados = 26%

# Usando o plotly para exibir nossa informações
# Passar informações que ira alimentar o eixo= x e eixo= y
# No histograma o eixo=y ja sera a quantidade sem necessidade de alimenta-lo
for coluna in tabela.columns:  # Laço para cada coluna criar um histogram
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    grafico.show()
''
# Com o grafico gerado conseguimos entender que os 10 primeiros meses são cruciais para o cliente cancelas os serviços
#


# Analise Top - Down (analise geral) como esta dividido esses cancelamentos, existe um padrao
# Analise Detalhada (Buscar a Solução)

# Visualizar a Base
html = tabela.to_html()
text_file = open("ResultadoGeral.html", "w")
text_file.write(html)
text_file.close()
webbrowser.open('ResultadoGeral.html')
