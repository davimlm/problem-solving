# Implemente um algoritmo que leia cinco valores e armazene-os em um vetor. Em seguida, mostre todos os valores lidos juntamente com a média dos valores.

# Ps: A média deve ser mostrada usando DUAS casas decimais.

# Importante: Neste exercício, não é permitido usar funções prontas em listas. Por exemplo: min, max, del, in, sort, reverse, index, count, etc. Também não é permitido usar print(*vetor) para mostrar o conteúdo de um vetor automaticamente.

# Para este exercício, os seguintes testes serão executados:

# ENTRADAS 1:
# 7
# 4
# 3
# 2
# 1
# SAÍDAS 1:
# 7 4 3 2 1
# 3.40

# ENTRADAS 2:
# 5
# 4
# 37
# 8
# 6
# SAÍDAS 2:
# 5 4 37 8 6
# 12.00

soma = 0 
vec = []

for i in range (5):
    nota = int(input())
    vec.append(nota)
    soma += nota
    print (vec[i], end = " ")    
    
media = soma/5

print("")
print("%.2f"%(media))