# Faça um programa que leia dois vetores a e b com 3 elementos reais cada, que representam um ponto no espaço tridimensional (cada elemento dos vetores é o valor de uma coordenada espacial). Os vetores devem ser lidos sequencialmente, isto é, primeiro lê-se o vetor a e depois o vetor b. Seu programa deve calcular a distância (d) entre estes dois pontos usando a fórmula:

# d = sqrt((ax - bx)**2 + (ay - by)**2 + (az - bz)**2)

# A saída do programa será: "A distância entre os dois pontos é d.", em que d deve ser formatado com 2 casas decimais.

import math

a = []
b = []

for i in range (3):
    x = float(input())
    a.append(x)

for j in range (3):
    y = float(input())
    b.append(y)
    
d = 0

for k in range (3):
    d += (a[k] - b[k])**2

print("A distância entre os dois pontos é %.2f."%(math.sqrt(d)))