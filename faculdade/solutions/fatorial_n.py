# Escreva um programa, usando a estrutura de repetição for, para calcular N! (fatorial de N). N! = N x (N-1) x (N-2) x ... x 2 x 1. Contudo, suponha que o valor a ser mostrado deve estar limitado a 1 milhão (por conta de restrição de memória do hardware em que o programa será usado).  Assim, o laço "for" deve ser interrompido caso o cálculo atinja este valor limite de um milhão. Você pode usar, por exemplo, uma variável booleana para indicar se o cálculo foi interrompido ou não.

# A entrada do programa é um inteiro N e a saída do programa deverá ser:

# "O fatorial de N é X.", com N e X inteiros e caso X seja até 1 milhão.
# Caso contrário a saída será: "Impossível calcular com as restrições de hardware.". 

# Lembre-se que o fatorial de zero é 1 e caso um número negativo seja inserido o seu programa deve retornar uma mensagem de erro: "Erro: o número deve ser um inteiro não negativo.". 

n = int(input())
facto = 1

for i in range (0, n, +1):
    facto *= (n - i)

if (n < 0):
    print ("Erro: o número deve ser um inteiro não negativo.")
elif (facto > 1000000):
    print ("Impossível calcular com as restrições de hardware.")
else:
    print("O fatorial de %d é %d."%(n, facto))