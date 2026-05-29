# Escreva um programa que leia duas matrizes A e B, de inteiros, de dimensões 3x3. Depois, o seu programa deve trocar, entre as matrizes A e B, todos os elementos que estão nos cantos (vértices) dessas matrizes. Após a troca, o programa deve mostrar as matrizes A e B, com um espaço entre elas. 

# Por exemplo, para a matriz de entrada A:

# 1 4 3
# 8 9 4
# 7 5 3
# e matriz de entrada B:

# 2 5 3
# 7 8 4
# 9 5 2
# seu programa deve imprimir:

# 2 4 3
# 8 9 4
# 9 5 2
# 1 5 3
# 7 8 4
# 7 5 3

#***********LENDOS AS MATRIZES***********
A = []

for i in range (3):
  linha_A = []
  for j in range (3):
    valor_A = int(input())
    linha_A.append(valor_A)
  A.append(linha_A)
      
B = []

for i in range (3):
  linha_B = []
  for j in range (3):
    valor_B = int(input())
    linha_B.append(valor_B)
  B.append(linha_B)

#*********** TRANSFORMANDO & PRINTANDO AS MATRIZES ***********
for i in range (3):
  for j in range (3):
    if (i == 0 and j == 0) or (i == 0 and j == 2) or (i == 2 and j == 0) or (i == 2 and j == 2):
      print(B[i][j], end = " ")
    else:
      print(A[i][j], end = " ")
  print()

print()
  
for i in range (3):
  for j in range (3):
    if (i == 0 and j == 0) or (i == 0 and j == 2) or (i == 2 and j == 0) or (i == 2 and j == 2):
      print(A[i][j], end = " ")
    else:
      print(B[i][j], end = " ")
  print()