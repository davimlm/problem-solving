# Implemente um programa, usando a estrutura de repetição while, que mostre uma contagem regressiva na tela, iniciando em NUM e terminando em 0 (inclua um caractere espaço entre cada número impresso). Vale ressaltar que NUM é definido pelo usuário e deve ser >=0, sendo que o programa deve ser finalizado SOMENTE quando o usuário digitar o NUM>=0. Além disso, uma mensagem "O numero deve ser >=0!" deve ser impressa, caso NUM<0. Por fim, uma mensagem “FIM!” será mostrada após a contagem.

# Os seguintes testes serão executados:

# ENTRADAS 1:
# -7
# 3

# SAÍDAS 1:
# O numero deve ser >=0!
# 3  2  1  0
# FIM!

# ENTRADA 2:
# 8

# SAÍDA 2:
# 8  7  6  5  4  3  2  1  0
# FIM!

num = int(input())

while(num < 0):
    print("O número deve ser >=0!")
    num = int(input())

while (num != -1 and num > -1):
    print(num, end= ' ')
    num = num - 1
print("")
print("FIM!")