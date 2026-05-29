# Escreva um programa que leia duas matrizes A e B, de inteiros, de dimensões 3x3. Depois, o seu programa deve criar e mostrar outra matriz C que seja a intersecção das matrizes A e B. A matriz intersecção deve trazer valor zero se os elementos nas mesmas posições das matrizes A e B forem diferentes; caso contrário, deve trazer o próprio elemento presente em A e B. 

# Por exemplo, para a matriz de entrada A:
# 1 5 3
# 8 9 4
# 7 5 3

# e matriz de entrada B:
# 2 5 3
# 7 8 4
# 9 5 2

# a matriz C, a ser mostrada pelo programa será:
# 0 5 3
# 0 0 4
# 0 5 0

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
  
C = []

for i in range (3):
  linha_C = []
  for j in range (3):
    if A[i][j] == B[i][j]:
      valor_C = A[i][j]
      linha_C.append(valor_C)
    else:
      valor_C = 0
      linha_C.append(valor_C)
  C.append(linha_C)
      
for i in range (3):
  for j in range (3):
    print(C[i][j], end = " ")
  print()