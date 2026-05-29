# Implemente um algoritmo que leia três inteiros e imprima o maior número. Se todos os valores forem iguais imprimir a mensagem "Números Iguais!".
 
# Alguns testes que serão realizados:

# ENTRADAS 1:
# 1
# 2
# 3

# SAÍDA 1:
# Maior é: 3

# ENTRADAS 2:
# 3
# 2
# 1

# SAÍDA 2:
# Maior é: 3

# ENTRADAS 3:
# 2
# 3
# 1

# SAÍDA 3:
# Maior é: 3


# ENTRADAS 4:
# 2
# 2
# 2

# SAÍDA 4:
# Números Iguais!

num1 = int(input())
num2 = int(input())
num3 = int(input())

if (num1 > num2 and num1 > num3 or num1 == num2 and num1 > num3):
    print ("Maior é:", num1)
elif (num2 > num1 and num2 > num3 or num1 == num2 and num2 > num3):
    print ("Maior é:", num2)
elif (num3 > num2 and num3 > num1 or num3 == num2 and num3 > num1):
    print ("Maior é:", num3)
elif (num1 == num2 == num3):
    print ("Números Iguais!")