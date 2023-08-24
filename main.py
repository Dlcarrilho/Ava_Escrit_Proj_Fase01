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
        cabecario = True
        dados = []
        for coluna in leitor:
          if (cabecario):
            cabecario = False
          else:
            dados.append(coluna)
        return dados
     
## GRAVADOR DE DADOS EM CSV






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

   
# Pergunta 1: Qual o percentual de jogos gratuitos e pagos na plataforma?
#Pergunta 2: Qual o ano com o maior número de novos jogos? Em caso de empate, retorne uma lista com os anos empatados.
#Pergunta 3:  Para demonstrar a facilidade de revisão e modificação de uso do módulo desenvolvido, uma pergunta 