# Faça um programa, usando a estrutura de repetição while, que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem CRESCENTE em uma linha. Depois, imprima esses números em ordem DECRESCENTE em outra linha. Inclua um caractere espaço entre cada número impresso.

# Dica 1: para imprimir a saída na mesma linha, é necessário especificar o parâmetro end="" no print (verifique se é necessário haver espaços em branco entre os termos!). O código a seguir, por exemplo, imprimirá o texto "abc" (sem espaços):

# print("a", end="")
# print("b", end="")
# print("c")
# Dica 2: algumas alternativas para concatenar duas strings sem incluir um espaço:

# print("a", "b", sep="") # especificando o parâmetro sep (é possível usar os parâmetros sep e end simultaneamente)
# print("a" + "b")
# print("a" + str(n)) # se n for um número, é necessário converter para str antes como indicado neste exemplo

# Os seguintes testes serão realizados,  

# ENTRADA 01:
# 10
# SAÍDAS 01:
# 0  1  2  3  4  5  6  7  8  9  10
# 10  9  8  7  6  5  4  3  2  1  0


# ENTRADA 02:
# 5
# SAÍDAS 02:
# 0  1  2  3  4  5
# 5  4  3  2  1  0

numeroN = int(input())
x = 0

while x <= numeroN:
    print(x, end=" ")
    x = x + 1
    
print("")

while x != 0:
    x = x - 1
    print (x, end=" ")
    