# Faça um programa que receba do usuário DOIS arrays, A e B, com 5 números inteiros cada. Crie um novo array C calculando C = A − B. Mostre na tela os dados do array C.

# Importante: Neste exercício, não é permitido usar funções prontas em listas. Por exemplo: min, max, del, in, sort, reverse, index, count, etc. Também não é permitido usar print(*vetor) para mostrar o conteúdo de um vetor automaticamente.

# Os seguintes testes serão executados:

# ENTRADAS 1:
# 1 
# 2
# 3
# 7
# 1
# 3
# 4
# 2
# 3
# 9
# SAÍDA 1:
# -2 -2 1 4 -8

# ENTRADAS 02:
# 3
# 2
# 1
# 4
# 3
# 0
# 9
# 2
# 6
# 5
# SAÍDA 2:
# 3 -7 -1 -2 -2

# ENTRADAS 03:
# -1
# -3
# -5
# 2
# 8
# 9
# -4
# -2
# 1
# 0
# SAÍDAS 3:
# -10 1 -3 1 8

import numpy as np 

a = []
b = []

for i in range (5):
    x = int(input())
    a.append(x)

for j in range (5):
    y = int(input())
    b.append(y)

for k in range (5):
    c = a[k] - b[k]
    print(c, end= " ")