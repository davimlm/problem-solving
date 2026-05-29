# Faça um programa que leia um número inteiro n, crie e mostre uma matriz n x n com elementos booleanos em que somente a moldura tenha valor True (os outros elementos são False. Veja os exemplos de saída. 

# Desafio: Você consegue usar compreensão de listas e criar a matriz, conforme requerida, usando somente uma linha de código?

# Exemplo de Entrada 1:
# 3
# Saída 1:
# TrueTrue True
# True False True
# True True True

# Exemplo de Entrada 2:
# 4
# Saída 2:
# True True True True
# True False False True
# True False False True
# True True True True

n = int(input())


for i in range (n):
  for j in range(n):
    if (i == 0) or (i == (n - 1)) or (j == 0) or (j == (n - 1)):
      print("True", end = " ") 
    else:
      print("False", end = " ")
  print()