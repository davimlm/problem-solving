# Faça um programa que leia dois conjuntos de números reais, armazenando-os nos vetores x e y e calcule o produto escalar entre eles. 

# Os conjuntos têm n = 5 elementos cada um e devem ser lidos da seguinte forma: primeiro leia todos os elementos do vetor x e depois leia todos os elementos do vetor y.

# Imprimir ambos os conjuntos e o produto escalar, dado por:

# x⋅y=∑i=0n−1(x[i]⋅y[i])

# A saída do programa será: "O produto escalar vale Pe.", em que Pe deve ser mostrado com duas casas decimais.

vec1 = []
vec2 = []

for i in range(5):
    x = float(input())
    vec1.append(x)

for j in range(5):
    y = float(input())
    vec2.append(y)

prodEsc = 0    
    
for k in range(5):
  prodEsc += vec1[k] * vec2[k]
  
print("O produto escalar vale %.2f."%prodEsc)