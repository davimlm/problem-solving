# Faça um programa que calcule o desvio padrão (σ) de um vetor v contendo n elementos reais, em que μ é a média do vetor.

# σ = sqrt((1 / (n - 1)) * Σ(i=0 até n-1) (v[i] - μ)^2)

# Seu programa deve primeiramente solicitar o valor n e depois realizar a leitura dos valores de v. A saída será: "O desvio padrão vale D.", em que D deve ser formatado com duas casas decimais.

import math

v= []

n = int(input())

media = 0

for i in range (n):
    x = float(input())
    media += x
    v.append(x)

media = media / n

somatorio = 0

for j in range (n):
    somatorio += (v[j] - media)**2

resultado = (somatorio / (n - 1))

print("O desvio padrão vale %.2f."%(math.sqrt(resultado)))