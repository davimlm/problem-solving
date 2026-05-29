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
# Após a leitura dos vetores, o programa deve imprimir os valores dos dois vetores (cada vetor em uma linha e os elementos devem ser separados pelo caractere espaço) e, ao final, deve-se imprimir "OK", se o vetor2 tem os mesmos valores do vetor1, mesmo que em ordem diferente, ou "Erro" caso contrário. Assuma não haver valores repetidos inseridos em cada vetor.

# Entradas 1: vetor1=[11, 33, 22]; vetor2=[11, 33, 22]
# Saídas 1:
# 11 33 22
# 11 33 22
# OK

# Entradas 2: vetor1=[11, 22, 33]; vetor2=[33, 11, 22]
# Saídas 2:
# 11 22 33
# 33 11 22
# OK

# Entradas 3: vetor1=[11, 22, 33]; vetor2=[11, 33, 55]
# Saídas 3: 
# 11 22 33
# 11 33 55
# Erro

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
  print ("Erro")
else:
  for k in range(n2):
      for l in range (n1):
          if vec2[k] == vec1[l]:
              ok += 1
  if ok == n1:
    print("OK")
  else:
    print("Erro")