# Escreva um programa que leia um valor n e depois os elementos de uma matriz A com dimensão n x n. Após isso, seu programa deve transformar a matriz A em uma matriz triangular inferior (com elementos somente abaixo da diagonal principal) e mostrá-la. 

# Por exemplo, para n = 3, e matriz A a seguir:
# 1 2 3
# 4 5 6
# 7 8 9

# A matriz a ser impressa, será:
# 0 0 0
# 4 0 0
# 7 8 0

n = int(input())

A = []
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input())
        linha.append(valor)
    A.append(linha)

for i in range(n):
    for j in range(n):
        if j >= i:
            A[i][j] = 0

for i in range(n):
    for j in range(n):
        print(A[i][j], end=" ")
    print()