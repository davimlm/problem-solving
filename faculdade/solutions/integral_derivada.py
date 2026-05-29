# Faça um programa que integre e derive polinômios. Cada polinômio é definido por um vetor que contém seus coeficientes, ordenados do maior para o menor grau.

# Por exemplo, o polinômio de grau dois 3𝑥**2+2𝑥+12 terá um vetor de coeficientes 𝑣=[3,2,12]. Sua integral será 𝐼=[1,1,12,0], equivalente ao polinômio x**3 + x**2 + 12x, e sua derivada será 𝐷=[6,2], equivalendo ao polinômio 6𝑥+2. O programa deve, primeiramente, receber o valor do maior grau 𝑔 do polinômio. Em seguida, deve ler (𝑔+1) coeficientes. Depois, calcular e mostrar (a) o vetor de coeficientes da integral do polinômio; e (b) o vetor de coeficientes da derivada do polinômio.

# Note que os coeficientes dos vetores da integral e da derivada são números reais e devem ser mostrados com duas casas decimais.
 

# Exemplo de Entradas:
# 2
# 3
# 2
# 12
# Saídas:
# 1.00 1.00 12.00 0.00
# 6.00 2.00

g = int(input())

vecPolinomio = []

for i in range (g + 1):
    x = int(input())
    vecPolinomio.append(x)
    
integral = 0

for j in range (g + 1):
    integral = vecPolinomio[j]/((g + 1) - j)
    print("%.2f"%(integral), end = " ")
    
print("0.00")    

derivada = 0

for k in range (g):
    derivada = vecPolinomio [k] * (g - k)
    print("%.2f"%(derivada), end = " ")