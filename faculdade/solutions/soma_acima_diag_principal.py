# Escreva um programa que leia um valor n e os elementos de uma matriz de inteiros com dimensões n x n (linha a linha). Depois, o programa deve calcular a soma dos elementos acima da diagonal principal. 

# Por exemplo, para uma matriz com n=3, definida a seguir, a saída do programa deverá ser: "A soma eh: 12", pois acima da diagonal principal estão 3 elementos  com valores 5, 3 e 4. Portanto, a soma é 5 + 3 + 4 = 12.

# 1 5 3
# 8 9 4
# 7 5 3

n = int(input())

sum = 0

for i in range (n):
  for j in range (n):
    valor = int(input())
    if i < j:
      sum += valor
      
print("A soma eh:", sum)