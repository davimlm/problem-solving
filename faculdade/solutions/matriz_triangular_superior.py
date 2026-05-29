# Faça um programa que leia um número inteiro n, crie e mostre uma matriz n x n triangular superior com valores iguais a 1. Uma matriz triangular superior possui somente os elementos acima da diagonal principal diferentes de zero. Veja os exemplos de saída. 

# Importante: Neste exercício, não é permitido usar funções prontas em listas. Por exemplo: min, max, del, in, sort, reverse, index, count, etc. Também não é permitido usar print(*vetor) para mostrar o conteúdo de um vetor automaticamente.

# Exemplo de Entrada 1:
# 2
# Saída 1:
# 0 1
# 0 0

# Exemplo de Entrada 2:
# 3
# Saída 2:
# 0 1 1
# 0 0 1
# 0 0 0
 
# Exemplo de Entrada 3:
# 4
# Saída 3:
# 0 1 1 1
# 0 0 1 1
# 0 0 0 1
# 0 0 0 0

n = int(input())

diagonal = 1

for i in range (n):
  for j in range (n):
    if j >= i + 1:
      print(diagonal, end = " ")
    else:
      print("0", end = " ")
  print()