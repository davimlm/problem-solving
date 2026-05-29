# Em matemática, o número harmônico designado por Hn define-se como o enésimo termo da série harmônica. Ou seja:

# Hn=1+1/2+1/3+1/4+...+1n

# Faça um programa, usando a estrutura de repetição for, que calcule o valor de qualquer Hn.

# PS: O Hn deve ser mostrado com UMA casa decimal.

# Não é permitido usar listas ou arrays do Python, ou de qualquer de suas bibliotecas.

# Os seguintes testes serão executados:

# ENTRADA 1:
# 2

# SAÍDA 1:
# 1.5

# ENTRADA 2:
# 100

# SAÍDA 2:
# 5.2

n = int(input())
nHarm = 0.0

for i in range (n, 0, -1):
    nHarm = nHarm + (1/i)
    
print("%.1f"%(nHarm))