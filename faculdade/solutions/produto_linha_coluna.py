# Escreva um programa que leia um valor n e depois os elementos de uma matriz A com dimensão n x n. Após isso, seu programa deve criar uma outra matriz B com dimensão n x n, em que os elementos de A são multiplicados por 3 caso o índice da linha seja par e multiplicados por -2 caso o índice da linha seja ímpar. Terminado o processamento, a matriz B deve ser impressa.

# Por exemplo, para n = 3, e matriz A a seguir:
# 1 2 3
# 4 5 6
# 7 8 9

# A matriz B, a ser impressa, será:
# 3 6 9
# -8 -10 -12
# 21 24 27

n = int(input())

A = []
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input())
        linha.append(valor)
    A.append(linha)

B = []
for i in range(n):
    linha = []
    for j in range(n):
        if i % 2 == 0:  
            linha.append(A[i][j] * 3)
        else:  
            linha.append(A[i][j] * -2)
    B.append(linha)

for i in range(n):
    for j in range(n):
        print(B[i][j], end=" ")
    print()