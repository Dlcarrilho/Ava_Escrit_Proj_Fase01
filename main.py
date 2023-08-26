# BIBLIOTECAS UTILIZADAS:

import random
import csv

# LEITOR DE ARQUIVO CSV
class Lercsv():

  def __init__(self, arquivo):
    
    self.arquivo = arquivo
    
  def abrirArq(self):
    with open(self.arquivo, 'r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv, delimiter = ',')
        cabecario = True # troca aqui
        dados = []
        for coluna in leitor:
          if (cabecario):
            cabecario = False
          else:
            dados.append(coluna)
        return dados
     
# GRAVADOR DE DADOS EM CSV - amostragem

class Gravar():
  def __init__(self, arq):
    self.arq = arq
 
  def gravar(self):
    a = open('amostragem.csv', 'w', newline='')
    w = csv.writer(a)
    for i in self.arq:
      w.writerow(i)

# GERADOR DE AMOSTRAGEM

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
    
# CALCULANDO O % DE JOGOS GRATUITOS E PAGOS

class Estatistica_venda():
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

# CONTAGEM - JOGOS/ANO
def dados(y):
  lista = []
  for index, ano in enumerate(y):
    lista.append(int(y[index][2].split()[2]))
  return lista
#### preparar dados para análise
def dic(z): # criar dicionário para ser utilizado na análise
  key_lista = []
  for index, ano in enumerate(z):
    if z[index] not in key_lista:
      key_lista.append(z[index])
  print("key lista", key_lista)

  contagem = []
  for ano in key_lista:
    contagem.append(z.count(ano))
  print('contagem', contagem)
  dic_contagem = dict(zip(key_lista, contagem)) # criar dicionário (ano: qtdes) / utilizado na estatística - lançamento dos jogos
  print(dic_contagem)

#### calcular estátistica de lançamento dos jogos no ano
class Estatistica_lancamento():
  def __init__(self, dicionario):
    self.dicionario = dicionario

  def maior_lanc(self):
    print(self.dicionario)














# CALCULANDO: ANO COM MAIOR NUMERO DE JOGOS + LISTA DE COMO OS ANOS EMPATADOS

a = Lercsv('amostragem.csv')
lerArq = a.abrirArq()

estPrice = Estatistica_venda(lerArq)
estPrice.est_calc()

dados = dados(lerArq)
dic = dic(dados)
dic = Estatistica_lancamento(dic)
dic.maior_lanc()


#e = Estatistica(lerArq)
#e.est_calc()


#Pergunta 2: Qual o ano com o maior número de novos jogos? Em caso de empate, retorne uma lista com os anos empatados.
#Pergunta 3:  Para demonstrar a facilidade de revisão e modificação de uso do módulo desenvolvido, uma pergunta 