# Faça um programa que leia um número inteiro n, crie e mostre uma matriz n x n preenchida com zeros, em que a diagonal principal seja composta por números negativos começando em -1 (na extremidade superior esquerda) até -n (na extremidade inferior direita). 

# Importante: Neste exercício, não é permitido usar funções prontas em listas. Por exemplo: min, max, del, in, sort, reverse, index, count, etc. Também não é permitido usar print(*vetor) para mostrar o conteúdo de um vetor automaticamente.

# Exemplo de Entrada 1:
# 2
# Saída 1:
# -1 0
# 0 -2

# Exemplo de Entrada 2:
# 3
# Saída 2:
# -1 0 0
# 0 -2 0
# 0 0 -3

n = int(input())

diagonal = 0

for i in range (n):
  for j in range (n):
    if j == i:
      diagonal = (-1 - i)
      print(diagonal, end = " ")
    else:
      print("0", end = " ")
  print()