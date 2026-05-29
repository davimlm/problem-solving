# Faça um programa, usando a estrutura de repetição for, que leia dois números inteiros N e s, e mostre uma sequência começando em N, cujos elementos sucessivos sejam decrementados de s, até que o último número seja maior ou igual a zero. Não é permitido usar listas ou arrays do Python, ou de qualquer de suas bibliotecas.

# Exemplo de execução:
# ENTRADAS:
# 10
# 3

# SAÍDA:
# 10 7 4 1

n = int(input()) 
s = int(input())

for i in range(n,-1,-s):
    print(i, end=" ")