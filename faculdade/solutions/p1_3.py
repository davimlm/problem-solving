# Um número triangular é um número natural que pode ser representado na forma de um triângulo equilátero:

# Em geral, o n-ésimo número triangular é dado por:

# T(n)=n×(n+1)2, n≥1

# Faça um programa que receba um valor inteiro N e imprima a sequência de números triangulares de 1 até N, separados por um espaço. Matematicamente: T(n) para n∈[1,...,N]. Além disso, o seu programa deve fornecer, na linha seguinte, a soma dos elementos pares da sequência de números triangulares.

# Exemplo:
# Entrada:
# 3
# Saída:
# 1 3 6
# 6

n = int(input())
cont = 1
tNPar = 0

while (cont<=n):
    tN = (cont*(cont+1))/2
    print("%.0f"%(tN), end = " ")
    
    if (tN % 2 == 0):
        tNPar += tN
        
    cont += 1


print("")

print("%.0f"%(tNPar))