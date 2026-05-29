# Faça um programa que LEIA do TECLADO um vetor de 10 posições e escreva na tela os números PARES e ÍMPARES. É importante destacar que o seu algoritmo NÃO deve imprimir, caso tiver, números PARES e ÍMPARES repetidos. Além disso, o MAIOR e MENOR número também deve ser impresso.

# Importante: Neste exercício, não é permitido usar funções prontas em listas. Por exemplo: min, max, del, in, sort, reverse, index, count, etc.

# Para este exercício, os seguintes testes serão executados:

# ENTRADAS 1:
# 2
# 4
# 5
# 3
# 1
# 7
# 6
# 5
# 4
# 3
# SAÍDAS 1:
# Números pares:
# 2
# 4
# 6
# Números impares:
# 5
# 3
# 1
# 7
# Maior: 7
# Menor: 1

 

# ENTRADAS 2:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# SAÍDAS 2:
# Números pares:
# 0
# 2
# 4
# 6
# 8
# Números impares:
# 1
# 3
# 5
# 7
# 9
# Maior: 9
# Menor: 0

# ENTRADAS 3:
# 2
# 2
# 4
# 4
# 6
# 6
# 6
# 8
# 8
# 8
# SAÍDAS 3:
# Números pares:
# 2
# 4
# 6
# 8
# Números impares:
# Maior: 8
# Menor: 2

vec = []
vecPar = []
vecImpar = []

for i in range(10):
    x = int(input())
    vec.append(x)

    j = 0
    while j < len(vecPar):
        if vecPar[j] == x:
            break
        j += 1

    if x % 2 == 0 and j == len(vecPar):
        vecPar.append(x)

    j = 0
    while j < len(vecImpar):
        if vecImpar[j] == x:
            break
        j += 1

    if x % 2 != 0 and j == len(vecImpar):
        vecImpar.append(x)

print("Números pares:")
for i in range(len(vecPar)):
    print(vecPar[i])

print("Números ímpares:")
for i in range(len(vecImpar)):
    print(vecImpar[i])

maior = vec[0]
menor = vec[0]

for j in range(1, 10):
    if vec[j] > maior:
        maior = vec[j]
    if vec[j] < menor:
        menor = vec[j]

print("Maior:", maior)
print("Menor:", menor)