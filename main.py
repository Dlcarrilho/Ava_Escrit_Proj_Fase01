## CARREGANDO ARQUIVO PARA ANALISE

arq = open("lista_games.csv")

for line in arq:
  lista = line.strip().split(',')
  print(lista)