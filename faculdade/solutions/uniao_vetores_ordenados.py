# Escreva um programa que, lidos dois vetores ordenados e sem valores repetidos v1 e v2, de tamanhos n1 e n2, respectivamente, retorne um vetor ordenado de tamanho n3, contendo todos os elementos não repetidos de v1 e v2. Internamente, v1 e v2 não possuem valores repetidos, mas podem ter valores que aparecem tanto em v1 como em v2!

# O programa deve primeiramente ler n1 e o conteúdo de v1. Depois, ler n2 e os valores em v2.

# Por exemplo, se n1= 4 com v1=[1, 2, 5, 8] e n2 = 3 com v2 = [0, 2, 9], o vetor a ser mostrado com os elementos separados por espaços, que representa a união dos dois vetores será [0, 1, 2, 5, 8, 9]. 

# Dica: você pode percorrer os índices dos dois vetores com um laço while, testando as condições em que os valores são maiores, menores ou iguais para ordenamento dos vetores. Observe que quando o teste dos dois vetores retornar valores iguais isso indicará valores repetidos! Outra possibilidade é, primeiramente, eliminar os valores repetidos de um dos vetores.

n1 = int(input())
v1 = []
v3 = []

for i in range (n1):
  x = int(input())
  v1.append(x)
  v3.append(x)
  
n2 = int(input())
v2 = []

for j in range (n2):
  y = int(input())
  v2.append(y)


for k in range(n2):
  i = 0
  
  while i < len(v3) and v2[k] != v3[i]:
    i += 1
  
  if i == len(v3):
    v3.append(v2[k])
     
maior = 0
      
for i in range (len(v3)):
  for j in range(len(v3) - 1):
    if v3[j] > v3[j + 1]:
      maior = v3[j]
      v3[j] = v3[j + 1]
      v3[j + 1] = maior
      
for j in range (len(v3)):
  print(v3[j], end = " ")