# Faça um programa que leia dois vetores 𝑥 e 𝑦 de 5 elementos inteiros cada um e crie um vetor 𝐼 que seja a intersecção entre os 2 vetores x e y. Ou seja, que contém somente os números que estão presentes em ambos os vetores. Os vetores devem ser lidos sequencialmente, isto é, primeiro lê-se o vetor 𝑥 e depois o vetor 𝑦. O vetor intersecção não deve conter números repetidos. Não use o operador "&" do Python.

# A saída do programa deverá ser: "O vetor intersecção é I", em que I é o vetor intersecção.

vec1 = []
vec2 = []
vecInt = []

for i in range(5):
    x = int(input())
    vec1.append(x)

for j in range(5):
    y = int(input())
    vec2.append(y)

print("O vetor intersecção é", end = " ")

for k in range(5):
  for l in range (5):
    if vec1[k] == vec2[l]:
      vecInt.append(vec1[k])
      
print("[", end= "")

for m in range (len(vecInt)):
  if (m + 1)== len(vecInt):
    print(vecInt[m], end= "")
  else:
    print(vecInt[m], end= ", ")

print("]")