# Leia uma matriz de tamanho 4 × 4. Em seguida, CONTE e ESCREVA na tela a quantidade de valores MAIORES do que 10 e também a quantidade de números NEGATIVOS. Após isso, os elementos da matriz também devem ser impressos.

# Por exemplo:
# ENTRADAS 01:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 1
# 2
# 3
# 4
# 5
# 6
# 7

# SAÍDAS 01:
# Maior que 10: 0
# Menor que 0: 0
# 1 2 3 4
# 5  6 7 8
# 9 1 2  3
# 4 5 6 7

 

# ENTRADAS 02:
# 4
# -2
# -3
# 56
# -9
# -5
# 12
# 32
# 1
# 2
# 3
# 4
# 32
# 98
# 8
# 7

# SAÍDAS 02:
# Maior que 10: 5
# Menor que 0: 4
# 4  -2 -3 56
# -9  -5 12 32
# 1 2  3  4
# 32 98 8 7

 

# ENTRADAS 03:
# -2
# -3
# 4
# -5
# -1
# 2
# 3
# 4
# 5
# 6
# 7
# 2
# 9
# 8
# 0
# 0

# SAÍDAS 03:
# Maior que 10: 0
# Menor que 0: 4
# -2 -3 4 -5
# -1 2 3 4
# 5 6 7 2
# 9 8 0 0

matriz = []

maior10 = 0
negativos = 0

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input())

        if valor > 10:
            maior10 += 1

        if valor < 0:
            negativos += 1

        linha.append(valor)

    matriz.append(linha)

print("Maior que 10:", maior10)
print("Menor que 0:", negativos)

for i in range(4):
    for j in range(4):
        print(matriz[i][j], end=" ")
    print()