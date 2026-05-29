# Uma empresa de logística gostaria de saber a distância a ser percorrida em diversas entregas.

# Escreva um programa que leia os valores de x e de y (coordenadas da empresa de logística). Após isso, leia um valor inteiro n e os n valores de um vetor. Todos os elementos do vetor são números inteiros. Esse vetor armazena as coordenadas das diversas entregas, com o seguinte formato: 1, y1, x2, y2, x3, y3, ... , xn/2, yn/2]. Ou seja, a cada duas posições no vetor, há uma coordenada (x, y).

# Após a leitura dos valores, o programa deve imprimir os valores do vetor (separando cada elemento por um caractere espaço) e, ao final, deve-se imprimir a distância da empresa até cada entrega. Vale ressaltar que as distâncias devem ser impressas na mesma linha (separadas por um caractere espaço) e com duas casas decimais.

# Cálculo da distância: neste exercício, considere o seguinte cálculo para obter a distância:

# d = sqrt((x2 - x1)**2 + (y2 - y1)**2)

import math

x = int(input())
y = int(input())

n = int(input())

vecEne = []

for i in range (n):
  nVal = int(input())
  print(nVal, end = " ")
  vecEne.append(nVal)

print()

for j in range (0,n , 2):
  d = math.sqrt(((vecEne[j]-x)**2) + ((vecEne[j + 1] - y)**2))
  print("%.2f"%d, end = " ")