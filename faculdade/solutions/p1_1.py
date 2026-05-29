# Na antiga Mesopotâmia, o talento era usado pelos sumérios, acadianos e babilônios como unidade de medida de peso e, posteriormente, como moeda. Esse sistema usava a base 60 para suas subdivisões, de modo que 1 talento era dividido em 60 minas e 1 mina era subdividida em 60 siclos. Portanto, a relação era: 1 talento (t) = 60 minas (m) = 3600 siclos (s). 

# Os comerciantes tinham certa dificuldade de fazer, rapidamente, a soma dos valores das mercadorias no sistema talentos, minas e siclos (TMS) e encomendaram de você um programa que receba os valores de dois produtos e informe o valor final da compra. Seu programa deve ler 6 parâmetros, nesta ordem: 

# talentos (produto 1)
# minas (produto 1)
# siclos (produto 1)
# talentos (produto 2)
# minas (produto 2)
# siclos (produto 2)

# E mostrar o resultado desta forma:
# "Total dos produtos: T talentos, M minas e S siclos.", em que T, M e S são a quantidade de talentos, minas e siclos da soma dos produtos.

# EXEMPLO DE ENTRADA:
# 2
# 32
# 7
# 2
# 2
# 26

# EXEMPLO DE SAÍDA:
# Total dos produtos: 4 talentos, 34 minas e 33 siclos.

t1 = int(input())
m1 = int(input())
s1 = int(input())
t2 = int(input())
m2 = int(input())
s2 = int(input())

tFinal = t1 + t2
mFinal = m1 + m2
sFinal = s1 + s2

if (mFinal > 60):
    tFinal += 1
    mFinal = mFinal - 60

if (sFinal > 60):
    mFinal += 1
    sFinal = sFinal - 60

print("Total dos produtos: %d talentos, %d minas e %d siclos."%(tFinal, mFinal, sFinal))