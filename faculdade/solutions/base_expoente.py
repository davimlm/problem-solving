# Faça um programa, usando a estrutura de repetição for, que solicite dois números inteiros positivos, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 

# Não utilize a função de potência do Python (** ou pow).

# É proibido usar listas ou arrays do Python, ou de qualquer de suas bibliotecas.

# Os seguintes testes serão executados:

# ENTRADA 1:
# 2
# 3
# SAÍDA 1:
# 8

# ENTRADA 2:
# 3
# 8
# SAÍDA 2:
# 6561

a = int(input())
b = int(input())
result = 1

for i in range (b,0,-1):
    result = result*a

if (b == 0):
    result = 1
    print(result) 
else:
    print(result) 