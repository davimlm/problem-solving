# Escreva um programa que leia duas matrizes A e B, de inteiros, de dimensões 3x3 e, após, um inteiro n não negativo e menor que 3. Depois, o seu programa deve trocar as linhas de índice correspondente a n das matrizes A e B, considerando os valores negativos. Após a troca, o programa deve mostrar as matrizes A e B, com um espaço entre elas. 

# Por exemplo, para a matriz de entrada A:

# 1 4 3
# 8 9 4
# 7 5 3
# e matriz de entrada B:

# 2 5 3
# 7 8 4
# 9 5 2
# e n = 0, seu programa deve imprimir:

# -2 5 3
# 8 9 4
# 7 5 3
# -1 4 -3
# 7 8 4
# 9 5 2

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
  
n = int(input())


#*********** TRANSFORMANDO & PRINTANDO AS MATRIZES ***********
for i in range (3):
  for j in range (3):
    if i == n:
      print(B[i][j], end = " ")
    else:
      print(A[i][j], end = " ")
  print()

print()
  
for i in range (3):
  for j in range (3):
    if i == n:
      print(A[i][j], end = " ")
    else:
      print(B[i][j], end = " ")
  print()