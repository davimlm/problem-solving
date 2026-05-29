# Faça um programa, usando a estrutura de repetição for, que leia n e mostre o valor S que é calculado da seguinte forma:

# S=1/1+2/3+3/5+4/7+5/9+...+nm

# O valor de S deve ser mostrado com DUAS casas decimais.

# Não é permitido usar listas ou arrays do Python ou de qualquer de suas bibliotecas.

# Os seguintes testes serão executados:

# ENTRADA 1:
# 2
# SAÍDA 1:
# 1.67

# ENTRADA 2:
# 5
# SAÍDA 2:
# 3.39

# ENTRADA 3:
# 9
# SAÍDA 3:
# 5.54

s = int(input())
iAnt = 1
cont = 1
soma = 0

for i  in range (1, (s+ 1), +1):
    if (i == 1):
        soma = 1
        i += 1
    else:
        iAnt += 2
        soma += ((i)/(iAnt))

print("%.2f"%(soma))