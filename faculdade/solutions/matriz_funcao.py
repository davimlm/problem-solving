# Faça um programa que leia um número inteiro N e crie uma matriz m de números inteiros com dimensão N x N. Cada elemento na matriz é dado em função dos índices da linha (l) e da coluna (c) da matriz, da forma m[l][c]=l3+2l2c2−3lc+c3
# . Depois, o programa deve mostrar todos os valores na diagonal secundária da matriz. Veja o exemplo. 

# Importante: Neste exercício, não é permitido usar funções prontas em listas. Por exemplo: min, max, del, in, sort, reverse, index, count, etc. Também não é permitido usar print(*vetor) para mostrar o conteúdo de um vetor automaticamente.

# Exemplo:
# Para a entrada N = 4, a matriz m é:
# 0 1 8 27
# 1 1 11 37
# 8 11 36 89
# 27 37 89 189

# A diagonal secundária é:
# 27 11 11 27

# Entrada:
# 4

# Saída:
# 27 11 11 27

n = int(input())
val = 0

for i in range (n):
  for j in range (n):
    val = (i**3) + (2*(i**2)*(j**2)) - (3*(i*j)) + (j**3)
    if j == (n - i) - 1:
      print(val, end = " ")