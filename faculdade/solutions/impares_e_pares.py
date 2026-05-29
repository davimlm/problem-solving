# Faça um programa, usando a estrutura de repetição while, que leia um número inteiro N e depois imprima os N primeiros números naturais ÍMPARES em uma linha e os N primeiros PARES em outra linha. Inclua um caractere espaço entre cada número impresso.

# Os seguintes testes serão realizados:

# ENTRADA 01:

# 10

# SAÍDAS 01:

# 1 3 5 7 9 11 13 15 17 19 
# 0 2 4 6 8 10 12 14 16 18

# ENTRADA 02:
# 5

# SAÍDAS 02:
# 1 3 5 7 9
# 0 2 4 6 8

n = int(input())
contadorPar = 0
contadorImpar = 0
numerosPares = 0
numerosImpares = 1

while(n > contadorImpar):
    print(numerosImpares, end = " ")
    numerosImpares = numerosImpares + 2
    contadorImpar = contadorImpar + 1
    
print("")

while(n > contadorPar):
    print(numerosPares, end = " ")
    numerosPares = numerosPares + 2
    contadorPar = contadorPar + 1