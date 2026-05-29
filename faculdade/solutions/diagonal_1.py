# Implemente um algoritmo que declare uma matriz com a mesma quantidade de linhas e colunas (DEFINIDA pelo USUÁRIO). Preencha com 1 a DIAGONAL PRINCIPAL e com 0 as OUTRAS POSIÇÕES da matriz. Ao final, ESCREVA a matriz obtida na tela.

# IMPORTANTE: Neste exercício, não é permitido usar funções prontas em listas. Por exemplo: min, max, del, in, sort, reverse, index, count, etc. Também não é permitido usar print(*vetor) para mostrar o conteúdo de um vetor automaticamente.

# Por exemplo:
# ENTRADA 01:
# 5
# SAÍDA 01:
# 1 0 0 0 0
# 0 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 0
# 0 0 0 0 1
 
# ENTRADA 02:
# 2
# SAÍDA 02:
# 1 0
# 0 1

# ENTRADA 03:
# 10
# SAÍDA 03:
# 1 0 0 0 0 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 0 0
# 0 0 0 1 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0 0 0
# 0 0 0 0 0 1 0 0 0 0
# 0 0 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 1 0 0
# 0 0 0 0 0 0 0 0 1 0
# 0 0 0 0 0 0 0 0 0 1

n = int(input())

for i in range(n):
    for j in range(n):
        if i == j:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()