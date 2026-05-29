# Escreva um programa que leia um número inteiro positivo 𝑛 e em seguida imprima 𝑛 linhas do chamado Triângulo de Pascal, conforme o exemplo para n = 6.

n = int(input())

vAnterior = []
vAtual = []

colunas = 0

for i in range (n + 1):
  vAnterior = vAtual
  vAtual = []

  for j in range (i):
    if j == 0 or j == i - 1:
      colunas = 1
      vAtual.append(colunas)
      print(colunas, end = " ")
      
    else:
      colunas = vAnterior[j - 1] + vAnterior[j]
      vAtual.append(colunas)
      print(colunas, end = " ")
    
  print()