# Escreva um programa que:

# Leia um valor inteiro n, depois leia os n valores de um vetor.
# Imprima os elementos do vetor lido (separe cada elemento por um caractere espaço).
# Após isso, leia um índice i e remova o elemento na posição i do vetor. Neste exercício, para remover um elemento, desloque uma posição para a esquerda os elementos que vem depois do índice removido (inclua um valor -1 na última posição do vetor). Exemplo: remover o elemento no índice 3 do vetor [11, 55, 66, 99, 33, 22, 77, 88]. Após a remoção: [11, 55, 66, 33, 22, 77, 88, -1].
# Imprima os elementos do vetor após a remoção (separe cada elemento por um caractere espaço).

n = int(input())
vec = []

for i in range (n):
    x = int(input())
    vec.append(x)
    print(x, end= " ")
    
print()

indice = int(input())

for j in range(n):
    if j < indice:
        print(vec[j], end = " ")
        
    elif j >= indice and j < n - 1:
        print(vec[j + 1], end = " ")
        
    elif j == n - 1:
        print(-1)