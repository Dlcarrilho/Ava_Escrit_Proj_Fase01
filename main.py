## BIBLIOTECAS UTILIZADAS:

import random
import csv

# LEITOR DE ARQUIVO CSV
class Lercsv():

  def __init__(self, arquivo):
    
    self.arquivo = arquivo
    
  def abrirArq(self):
    with open(self.arquivo, 'r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv, delimiter = ',')
        cabecario = False
        dados = []
        for coluna in leitor:
          if (cabecario):
            cabecario = False
          else:
            dados.append(coluna)
        return dados
     
## GRAVADOR DE DADOS EM CSV - amostragem

class Gravar():
  def __init__(self, arq):
    self.arq = arq
 
  def gravar(self):
    a = open('amostragem.csv', 'w', newline='')
    w = csv.writer(a)
    for i in self.arq:
      w.writerow(i)

## GERADOR DE AMOSTRAGEM

class Amostra():
  def __init__(self, amostra):
    self.amostra = amostra
  
  def gerar_amostra(self):
    amostragem = []
    for a in range(0,20):
      y = random.choice(self.amostra) 
      if y not in amostragem: # garantindo que não escolha o mesmo elemento mais de uma vez
        amostragem.append(y)
    return amostragem
    
## CALCULANDO O % DE JOGOS GRATUITOS E PAGOS

class Estatistica():
  def __init__(self, lista):
        self.lista = lista
  
  def est_calc(self):
    valor_maior_zero = []
    valor_menor_igual_zero = []
    for p in range(len(self.lista)):
      
      if float(self.lista[p][6]) != 0:
        valor_maior_zero.append(self.lista[p][6])
      else:
        valor_menor_igual_zero.append(self.lista[p][6])
    
    tam_amostra = len(valor_maior_zero) + len(valor_menor_igual_zero)
    per_gratuitos = round(float(len(valor_menor_igual_zero) / tam_amostra),3)
    per_pagos =  round(1- float(len(valor_menor_igual_zero) / tam_amostra),3)
    print(f'==> Percentual de Jogos Gratuitos: {per_gratuitos} | Percentual de jogos pagos: {per_pagos}  <==')

## CALCULANDO: ANO COM MAIOR NUMERO DE JOGOS + LISTA DE COMO OS ANOS EMPATADOS

a = Lercsv('amostragem.csv')
lerArq = a.abrirArq()
lista = []

def lista_ano(y):
  for count, ano in enumerate(y):
    lista.append(int(y[count][2].split()[2]))
  return lista

  

#Pergunta 2: Qual o ano com o maior número de novos jogos? Em caso de empate, retorne uma lista com os anos empatados.
#Pergunta 3:  Para demonstrar a facilidade de revisão e modificação de uso do módulo desenvolvido, uma pergunta 