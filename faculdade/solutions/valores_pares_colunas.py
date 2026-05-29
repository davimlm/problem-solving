# Escreva um programa que leia a quantidade de linhas (n_linhas) e colunas (n_colunas) de uma matriz. Após isso, crie uma matriz (n_linhas x n_colunas) com valores PARES, iniciando com zero (0), que devem ser preenchidos coluna por coluna. Por fim, imprima a matriz com um caractere espaço entre os elementos.

# Por exemplo, para n_linhas=3 e n_colunas=6, a seguinte matriz deve ser impressa:

# 0 6 12 18 24 30
# 2 8 14 20 26 32
# 4 10 16 22 28 34

n_linhas = int(input())
n_colunas = int(input())

soma = 0

for i in range(n_linhas):
  i *= 2
  for j in range (n_colunas):
    if j == 0:
      soma = i
    else:
      soma += 6
      
    print(soma, end = " ")
  print()