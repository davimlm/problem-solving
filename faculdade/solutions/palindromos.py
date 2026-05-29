# Faça um programa que teste se uma palavra ou número é um palíndromo. Se uma palavra pode ser lida, indiferentemente, da esquerda para a direita e vice-versa, ela é considerada um palíndromo. Mesma coisa com um número.

# Exemplo: 
# A palavra RAIAR é um palíndromo porque pode ser lida (com o mesmo significado) tanto da esquerda para a direita como da direita para a esquerda.
# A sequência 12321 é um palíndromo porque pode ser lida (com o mesmo quantitativo) tanto da esquerda para a direita como da direita para a esquerda.

# Você deve ler a palavra ou o número a ser testado. O seu programa deverá imprimir as seguintes mensagens “É um palíndromo” (caso seja um palíndromo) ou “Não é um palíndromo” (caso não seja um palíndromo).

palavra = str(input())
contIguais = 0

for i in range (len(palavra)):
    if palavra[i] == palavra[len(palavra) - 1 - i]:
        contIguais += 1
        
if contIguais == len(palavra):
    print("É um palíndromo")
else:
    print("Não é um palíndromo")