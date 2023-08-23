## BIBLIOTECAS UTILIZADAS:

import random
import numpy

## CARREGANDO ARQUIVO PARA ANALISE

arq = open("lista_games.csv")
dataset = []
amostragem = []

primeira = True
for line in arq:
  if primeira:
    primeira = False
    continue
  linhas = line.strip().split(',')
  dataset.append(linhas)

## GERADOR DE AMOSTRAGEM

def amostraAleatoria(y):
  return random.choice(y)

#### GERANDO AMOSTRA
for a in range(0,20):
  y = amostraAleatoria(dataset) 
  if y not in amostragem: # garantindo que não escolha o mesmo elemento mais de uma vez
    amostragem.append(y)

## CALCULANDO O % DE JOGOS GRATUITOS E PAGOS
valor_maior_zero = []
valor_menor_igual_zero = []
for p in range(len(amostragem)):
  if float(amostragem[p][7]) > 0:
    valor_maior_zero.append(amostragem[p][7])
  else:
    valor_menor_igual_zero.append(amostragem[p][7])
    
tam_amostra = len(valor_maior_zero) + len(valor_menor_igual_zero)
per_gratuitos = round(float(len(valor_menor_igual_zero) / tam_amostra),3)
per_pagos =  round(1- float(len(valor_menor_igual_zero) / tam_amostra),3)
print(f'==> Percentual de Jogos Gratuitos: {per_gratuitos} | Percentual de jogos pagos: {per_pagos}')
  
# Pergunta 1: Qual o percentual de jogos gratuitos e pagos na plataforma?
#Pergunta 2: Qual o ano com o maior número de novos jogos? Em caso de empate, retorne uma lista com os anos empatados.
#Pergunta 3:  Para demonstrar a facilidade de revisão e modificação de uso do módulo desenvolvido, uma pergunta 