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
  lista = line.strip().split(',')
  dataset.append(lista)
  #print(lista)

## Gerador de Amostragem - 20 observações

def amostraAleatoria(dataset):
  return random.choice(dataset)

for a in range(0,4):
  amostragem.append(amostraAleatoria(dataset))
  print(amostragem[a][0])
  





  
# Pergunta 1: Qual o percentual de jogos gratuitos e pagos na plataforma?
#Pergunta 2: Qual o ano com o maior número de novos jogos? Em caso de empate, retorne uma lista com os anos empatados.
#Pergunta 3:  Para demonstrar a facilidade de revisão e modificação de uso do módulo desenvolvido, uma pergunta 