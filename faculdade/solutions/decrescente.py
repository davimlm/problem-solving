# Leia dois números do tipo float e apresente-os em ordem decrescente. Suponha que não sejam iguais.
 
# Os seguintes testes serão realizados,   

# ENTRADA 1:
# 3.0
# 2.0

# SAÍDA 1:
# 3.0
# 2.0

# ENTRADA 2:
# 1.4
# 10.5

# SAÍDA 2:
# 10.5
# 1.4

numero1 = float(input())
numero2 = float(input())

if (numero1 > numero2):
    print(numero1)
    print(numero2)
else:
    print(numero2)
    print(numero1)