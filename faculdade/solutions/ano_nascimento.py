# Implemente um algoritmo que leia, via teclado, o ano de nascimento de uma pessoa, o ano atual e mais outro ano no futuro. Depois, calcule e mostre:

# a) A idade dessa pessoa;
# b) Quantos anos essa pessoa terá em um determinado ano definido, via teclado, pelo usuário.
 
# Assuma que a pessoa já tenha feito aniversário no ano atual.
 
# Dica para impressão:
 
# A impressão do valor de uma variável no meio de uma frase pode ser realizada das seguintes formas:
 
# print("Em ", ano, ", a idade sera: ", idade, sep="")
# OU
# print("Em {0}, a idade sera: {1}".format(ano, idade))
# OU
# print("Em %d, a idade sera: %d"%(ano,idade))
 
 
# Os seguintes testes serão realizados (observe o formato das saídas)

# ENTRADAS 1:
# 1980
# 2021
# 2025

# SAÍDAS 1:
# Idade atual: 41
# Em 2025, a idade sera: 45

# ENTRADAS 2:
# 1993
# 2021
# 2030

# SAÍDAS 2:
# Idade atual: 28
# Em 2030, a idade sera: 37

anoNascimento = int(input())
anoAtual = int(input())
anoFuturo = int(input()) 

idadeAtual = (anoAtual - anoNascimento)
idadeFutura = (anoFuturo - anoNascimento)

print ("Idade atual:", idadeAtual)
print ("Em %d, a idade sera: %d" % (anoFuturo, idadeFutura))