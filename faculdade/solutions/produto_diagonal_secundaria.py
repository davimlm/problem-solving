# Escreva um programa que leia um valor n e os elementos de uma matriz de inteiros com dimensões n x n (linha a linha). Depois, o programa deve calcular o produto dos elementos na diagonal secundária da matriz. 

# Por exemplo, para n=3 e a matriz a seguir, a saída do programa deverá ser: "O produto é: 189", pois na diagonal secundária estão 3 elementos  com valores 3, 9 e 7. Portanto, o produto é 3 * 9 * 7 = 189.

# 1 5 3
# 8 9 4
# 7 5 3

n = int(input())

vecProd = []

prod = 1

for i in range(n):
  for j in range(n):
    valor = int(input())
    
    if i + j == 2:
      prod *= valor
      
print(prod)