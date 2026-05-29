# Implemente um algoritmo que leia do teclado SEIS valores inteiros e em seguida mostre na tela os valores lidos na ORDEM INVERSA.

# Importante: Neste exercício, não é permitido usar funções prontas em listas. Por exemplo: min, max, del, in, sort, reverse, index, count, etc. Também não é permitido usar print(*vetor) para mostrar o conteúdo de um vetor automaticamente.

# Alguns testes que serão executados:

# ENTRADAS 01:
# 1
# 2
# 3
# 4
# 5
# 6
# SAÍDAS 01:
# 6 5 4 3 2 1

# ENTRADAS 02:
# 6
# 5
# 4
# 3
# 2
# 1
# SAÍDAS 02:
# 1 2 3 4 5 6

vec = []

for i in range (6):
    x = int(input())
    vec.append(x)
    

for j in range (5, -1, -1):
    print(vec[j], end = " ")