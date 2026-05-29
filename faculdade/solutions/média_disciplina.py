# Um professor calcula a nota do curso (N) da seguinte forma:

# N = 0,40 x P1 + 0,45 x P2 + 0,15 x MEPP

# Neste cálculo, P1 é a nota da Prova 1, P2 é a nota da Prova 2 e MEPP é a média das notas das atividades práticas.

# Escreva um programa que leia as notas P1, P2 e MEPP. Após isso, imprima o valor de N.

# Observação: imprima o valor usando duas casas decimais. Para formatar a saída em Python é possível utilizar, por exemplo, o seguinte código:

# numero = 5.07507
# print("%.2f"%(numero))

# Entrada:
# P1
# P2
# MEPP

# Saída:
# N

p1 = float(input())
p2 = float(input())
mepp = float(input()) 

notaFinal = (0.4*p1) + (0.45*p2) + (0.15*mepp)

print("%.2f"%(notaFinal))