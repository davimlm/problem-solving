# Escreva um programa, usando a estrutura de repetição while, para cadastrar e calcular a média de idade de N adolescentes que participarão de uma pesquisa científica. Nesse caso, considera-se adolescente como uma pessoa com idade entre 12 anos completos e 18 anos incompletos.

# O programa deve receber primeiramente o valor de N (maior que 2). Depois, deve solicitar repetidamente os dados das idades até que o número de adolescentes estipulado seja atingido. Observe que o usuário pode digitar valores de idades que não são de adolescentes e, portanto, o programa pode precisar ler um número de idades maior que N, pois a leitura deve finalizar somente quando tiverem sido obtidas N idades de adolescentes.

# Quando a quantidade N de idades de adolescentes for atingida, o programa deve calcular a média das idades (somente dos N adolescentes) e imprimir uma mensagem conforme exemplo:

# "A idade media dos N adolescentes é m anos.", em que N é o número de adolescentes e m é a média das idades, mostrada com uma casa decimal.

# Caso o usuário entre com N menor ou igual a 2 uma mensagem de erro deve aparecer: "Poucos participantes para a pesquisa.".

n = int(input())
nInalt = n
idade = 0
idadeSoma = 0
contAdo = 0
media = 0

if (n<=2):
    print("Poucos participantes para a pesquisa.")
else:
    while(n > 0):
        idade = int(input())
        
        if (idade >= 12 and idade < 18):
            contAdo += 1
            n -= 1
            idadeSoma += idade
            
    media = idadeSoma/nInalt
    print("A idade media dos %d adolescentes é %.1f anos."%(contAdo, media))