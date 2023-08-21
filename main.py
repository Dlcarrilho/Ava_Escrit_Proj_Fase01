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



  
# Pergunta 1: Qual o percentual de jogos gratuitos e pagos na plataforma?
#Pergunta 2: Qual o ano com o maior número de novos jogos? Em caso de empate, retorne uma lista com os anos empatados.
#Pergunta 3:  Para demonstrar a facilidade de revisão e modificação de uso do módulo desenvolvido, uma pergunta 