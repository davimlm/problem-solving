# Realizou-se uma pesquisa com 3 pessoas que responderam à seguinte pergunta:

# Quantos filhos você tem?

# Escreva um algoritmo para processar essa pesquisa informando quantas pessoas possuem até 2 filhos e quantas possuem mais de 2 filhos.

# Os seguintes testes serão realizados,  

# ENTRADAS 01:
# 1
# 2
# 1

# SAÍDAS 01:
# Até dois filhos: 3
# Mais de dois filhos: 0

# ENTRADAS 02:
# 3
# 4
# 5
# SAÍDAS 02:
# Até dois filhos: 0
# Mais de dois filhos: 3

# ENTRADAS 03:
# 1
# 4
# 2
# SAÍDAS 03:
# Até dois filhos: 2
# Mais de dois filhos: 1


# ENTRADAS 04:
# 1
# 5
# 3
# SAÍDAS 04:
# Até dois filhos: 1
# Mais de dois filhos: 2

pessoa1 = int(input())
pessoa2 = int(input())
pessoa3 = int(input())


if (pessoa1 > 2):
    maisDoisFilhos = maisDoisFilhos + 1
else:
    ateDoisFilhos = ateDoisFilhos +1
    
if (pessoa2 > 2):
    maisDoisFilhos = maisDoisFilhos + 1
else:
    ateDoisFilhos = ateDoisFilhos + 1
    
if (pessoa3 > 2):
    maisDoisFilhos = maisDoisFilhos + 1 
else:
    ateDoisFilhos = ateDoisFilhos + 1
    
print ("Até dois filhos:", ateDoisFilhos)
print("Mais de dois filhos:", maisDoisFilhos)