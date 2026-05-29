# Escreva um programa que leia um valor inteiro n1, depois leia os n1 valores de um vetor1. Após isso, leia um valor inteiro n2 e os n2 valores de um vetor2. Todos os elementos dos vetores são números inteiros.

# Observe que os valores de entrada são apresentados cada um em uma linha. Por exemplo:

# n1=3
# 11
# 33
# 22
# n2=4
# 55
# 44
# 77
# 66
# Após a leitura dos vetores, o programa deve imprimir os valores dos dois vetores (cada vetor em uma linha, separe cada elemento por um caractere espaço) e, ao final, imprima "Vetor duplicado" se os valores no vetor1 são o dobro dos valores nas posições correspondentes no vetor2 ou "Erro" caso contrário. 

# Neste exercício, considere que um vetor é duplicado se tem o mesmo TAMANHO do outro vetor e se os valores em cada índice do vetor1 são iguais ao dobro dos valores nas posições correspondentes no vetor2. Por exemplo: para os vetores [22, 66, 44] e [11, 33, 22], deve-se imprimir "Vetor duplicado".

n1 = int(input())
vec1 = []

for i in range(n1):
  x = int(input())
  vec1.append(x)
  print(x, end = " ")
    
n2 = int(input())
vec2 = []
print()

for j in range(n2):
  y = int(input())
  vec2.append(y)
  print(y, end = " ")
  
print()

ok = 0

if n1 != n2:
  print("Erro")
else:
  for k in range(n1):
    if (vec1[k]) == 2*vec2[k]:
      ok += 1
      
  if ok == n2 and n1 == n2:
    print("Vetor duplicado")
  else:
    print("Erro")