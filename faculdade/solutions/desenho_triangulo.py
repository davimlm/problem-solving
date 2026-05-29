# Escreva um programa que desenhe um triângulo, usando um determinado caractere determinado pelo usuário, que tenha uma base ímpar b com uma altura igual a h = ceil(b/2). A operação ceil(x) retorna o menor número inteiro que seja maior ou igual a x. Por exemplo, ceil(3.44) = 4.

# Seu programa deve primeiramente testar se b é ímpar. Caso não seja, deve retornar a mensagem de erro: "A base do triângulo deve ser um número ímpar.". Caso o valor de b seja ímpar, o programa deve prosseguir com a leitura do caractere a ser usado para o desenho e com o desenho do triângulo propriamente dito.

# Não é permitido usar listas ou arrays do Python, ou de qualquer de suas bibliotecas.

# Como exemplo, se b = 7 e o caractere for "*", seu programa deve desenhar o seguinte:

#    * 

#   ***

#  *****

# *******

# Dica: considerando um retângulo b x h, preencha as posições que não pertencem ao triângulo com um espaços.

import math

b = int(input("Digite a base do triângulo: "))

if b % 2 == 0:
    print("A base do triângulo deve ser um número ímpar.")
else:
    c = input("Digite o caractere para desenhar o triângulo: ")
    h = math.ceil(b / 2)

    for i in range(1, h + 1):
        espacos = h - i
        caracteres = 2 * i - 1

        for j in range(espacos):
            print(" ", end="")

        for j in range(caracteres):
            print(c, end="")

        print()