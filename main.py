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
      if y not in amostragem: # garantindo que ñ escolha o mesmo elemento mais de uma vez
        amostragem.append(y)
    return amostragem
    
# CALCULANDO O % DE JOGOS GRATUITOS E PAGOS

class Estatistica_venda():
  def __init__(self, lista):
        self.lista = lista
  
  def perfilVendas(self):
    print('*** ESTATISTICA - VENDAS/JOGOS ***')
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
    print(f'==> Percentual de Jogos Gratuitos: {per_gratuitos} | Percentual de jogos Pagos: {per_pagos}  <==')

# CALCULANDO QUANITDADE LANÇAMENTO POR ANO

class Estatistica_lancamento:
  def __init__(self, lerArq):
    
    self.lerArq = lerArq
  
  def qtdLan(self):
    print()
    print('*** ESTATISTICA - LANÇAMENTOS JOGOS/ANO ***')
    '''preparando a base para análise'''
    lista = []
    for index, ano in enumerate(self.lerArq):
      lista.append(int(self.lerArq[index][2].split()[2]))
    lista = lista
    key_lista = []
    for index, ano in enumerate(lista):
      if lista[index] not in key_lista:
        key_lista.append(lista[index])
    #print("key lista", key_lista)
  
    contagem = []
    for ano in key_lista:
      contagem.append(lista.count(ano))
    #print('contagem', contagem)
    dic_contagem = dict(zip(key_lista, contagem)) # criar dicionário (ano: qtdes)
    #print(dic_contagem)
    '''buscando o os valores repetidos (empate)'''
    emp = {}
    for key, value in dic_contagem.items():
        emp.setdefault(value, set()).add(key)
    
    result = [key for key, values in emp.items()
                                  if len(values) > 1]
    r = result
    #print(r)
    '''buscando o ano correspodente dos valores repetidos'''
    if len(r) > 0:
      ano_empates = []
      valor_empates = []
      for key, value in dic_contagem.items():
        if value in r:
          ano_empates.append(key)
          valor_empates.append(value)
      empate = sorted(dict(zip(ano_empates, valor_empates)).items())
      print('==> Exitem anos com a mesma quantidade de lancamentos (ano, qtdes) <==')
      print(empate)   

    '''buscando o ano com o maior lançamento'''
    maior = dic_contagem[max(dic_contagem, key=dic_contagem.get)]
    print(maior)
    for key, value in dic_contagem.items():
      if value == maior:
        ano = key
        qtde = value
    
    print()
    print(f'==> O ano como maior lançamento é {key} com {value} obvervação <==')
    
# CALCULANDO: ANO COM MAIOR NUMERO DE JOGOS + LISTA DE COMO OS ANOS EMPATADOS

arq = Lercsv('arquivo.csv')
abrir = arq.abrirArq()
a = Amostra(abrir)
gravar = a.gerar_amostra()
g = Gravar(gravar)
g.gravar()

amostragem = Lercsv('amostragem.csv')
amostra = amostragem.abrirArq()

Estatistica_venda = Estatistica_venda(amostra)
Estatistica_venda.perfilVendas()

Estatistica_lancamento = Estatistica_lancamento(amostra)
Estatistica_lancamento.qtdLan()

#Pergunta 2: Qual o ano com o maior número de novos jogos? Em caso de empate, retorne uma lista com os anos empatados.
#Pergunta 3:  Para demonstrar a facilidade de revisão e modificação de uso do módulo desenvolvido, uma pergunta 

