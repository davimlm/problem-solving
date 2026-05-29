# Implemente um algoritmo que leia uma matriz (inteiros) de tamanho 3 × 3 com números diferentes. Imprima na tela o menor valor e o maior valor contido nessa matriz, assim como a sua localização (linha e coluna). Após isso, os elementos da matriz também devem ser impressos.

# IMPORTANTE: Neste exercício, não é permitido usar funções prontas em listas. Por exemplo: min, max, del, in, sort, reverse, index, count, etc. Também não é permitido usar print(*vetor) para mostrar o conteúdo de um vetor automaticamente.

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

# SAÍDAS 01:
# Maior: 9
# Posição (maior): 2 linha e 2 coluna
# Menor: 1
# Posição (menor): 0 linha e 0 coluna
# 1 2 3 
# 4 5 6
# 7 8 9

matriz = []

n = 0

for i in range(3):
    linha = []  
    for j in range(3):
        valor = int(input())

        if n == 0:
            menor = valor
            maior = valor

            linhaMenor = i
            colunaMenor = j

            linhaMaior = i
            colunaMaior = j

            n += 1

        if valor > maior:
            maior = valor
            linhaMaior = i
            colunaMaior = j

        elif valor < menor:
            menor = valor
            linhaMenor = i
            colunaMenor = j

        linha.append(valor)

    matriz.append(linha)

print("Maior:", maior)
print("Posição (maior): %d linha e %d coluna" % (linhaMaior, colunaMaior))

print("Menor:", menor)
print("Posição (menor): %d linha e %d coluna" % (linhaMenor, colunaMenor))

for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=" ")
    print()