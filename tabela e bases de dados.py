import os
import pandas as pd
#import matplotlib.pyplot as plt
from pathlib import Path
import plotly.express as px

#LÓGICA DO DESAFIO:
#Passo 1: Percorrer todos os arquivos da pasta base de dados (Vendas)..

listaArquivos = os.listdir(f"{Path.cwd()}/vendas")
#print (listaArquivos)
#Passo 2: Importar bases de dados de vendas..
#Passo 3: Tratar/compilar as bases de dados..

tabelaTotal = pd.DataFrame()
for arquivo in listaArquivos:
  if "Vendas" in arquivo:
    #print (arquivo)
    #importando o arquivo..
    tabela = pd.read_csv(f"{Path.cwd()}/Vendas/{arquivo}")
    tabelaTotal = pd.concat([tabelaTotal, tabela], ignore_index=True)
    #print(tabela)
print("1: TABELA DE VENDAS")
print(tabelaTotal)

#Passo 4: Calcular o produto mais vendido em quantidade..
tabelaProdutos = tabelaTotal.groupby("Produto")[["Quantidade Vendida"]].sum().sort_values(by="Quantidade Vendida", ascending= False)
print("2: PRODUTOS MAIS VENDIDOS EM QUANTIDADE")
print (tabelaProdutos)
#print(tabelaTotal.info())

#Passo 5: Calcular o produto mais vendido em faturamento..
tabelaTotal["Faturamento"] = tabelaTotal["Quantidade Vendida"] * tabelaTotal["Preco Unitario"]
tabelaFaturamento = tabelaTotal.groupby("Produto")[["Faturamento"]].sum().sort_values(by="Faturamento", ascending= False)
print("3: PRODUTO MAIS VENDIDO (FATURAMENTO)")
print(tabelaFaturamento)

#Passo 6: Calcular a loja/cidade que mais vendeu em faturamento
tabelaLojas = tabelaTotal.groupby("Loja").sum()[["Faturamento"]]
#tabelaLojas = tabelaLojas[["Faturamento"]]
print("4: LOJA QUE MAIS VENDEU (EM FATURAMENTO)")
print(tabelaLojas)

#Passo 7: criar um gráfico/dashboard pra visualizar esses dados.
#plt.plot(tabelaLojas)
#plt.show()

graficoLojas = px.bar(tabelaLojas, x=tabelaLojas.index, y='Faturamento')
graficoLojas.show()

#graficoProdutos = px.bar(tabelaProdutos, x=tabelaProdutos.index, y='Quantidade Vendida')
#graficoProdutos.show()