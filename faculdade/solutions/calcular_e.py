# Faça um programa que LEIA um valor inteiro e positivo N, calcule e mostre o valor E, conforme a fórmula a seguir:

# E=1/1!+1/2!+1/3!+...+1/N!

# O valor de E deve ser mostrado com três casas decimais. Não pode ser utilizada a função factorial de qualquer biblioteca do Python. Portanto, evite usar o nome "factorial" em seu programa.

# Não é permitido usar listas ou arrays do Python, ou de qualquer de suas bibliotecas.

# Os seguintes testes serão executados:

# ENTRADA 1:
# 7
# SAÍDA 1:
# 1.718

# ENTRADA 2:
# 2
# SAÍDA 2:
# 1.500

n = int(input())
e = 0

for i in range (1, n+1, +1):
    facto = 1
    
    for j in range (1, i+1, +1):
        facto *= j
        
    e += 1/facto
        
print("%.3f"%(e))