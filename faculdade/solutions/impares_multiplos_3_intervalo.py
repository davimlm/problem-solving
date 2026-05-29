# Escreva um programa, usando a estrutura de repetição while, para ler as extremidades de um intervalo fechado [a, b] e contar a quantidade de números ímpares que também sejam múltiplos de 3 nesse intervalo.

# A saída do programa deve ser: "Tem c número(s) ímpar(es) múltiplo(s) de 3 entre a e b.", em que c é o número obtido pelo programa, e a e b são as extremidades do intervalo.

a = int(input())
b = int(input())
cont = a - 1
conditional = 0

while (cont < b):
    cont = cont + 1
    if(cont % 2 != 0 and cont % 3 == 0):
        conditional = conditional + 1

print ("Tem %d número(s) ímpar(es) múltiplo(s) de 3 entre %d e %d."%(conditional,a,b))