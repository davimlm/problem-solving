# Escreva um programa, usando a estrutura de repetição while, para ler N valores e determinar o menor entre aqueles que estiverem no intervalo fechado [a, b]. Seu programa deve receber primeiramente o valor N e os limites a e b, para só então ler os valores e efetuar o processamento requerido. 

# Caso não haja valores no intervalo, o programa deve emitir uma mensagem de erro do tipo: "Sem valores no intervalo definido.". Se houver valores, a saída do programa deve ser: "O menor valor no intervalo vale x.", em que x deve ter exatamente duas casas decimais. 

# Dica: para encontrar o menor valor você pode inicializar a respectiva variável como float('inf') e atualizá-la conforme os valores forem apresentados. 

# O float('inf') cria um número infinito e deve ser usado, por exemplo, da seguinte forma:

# a = float('inf')

# Neste caso, o valor de a será um número infinito.

n = int(input())
a = int(input())
b = int(input())
menor = 0
valores = 0

while (n > 0):  
    valores = float(input())
    if(valores >= a and valores <= b): 
        if(menor == 0):
            menor = valores
        elif (valores < menor):
            menor = valores

    n = n - 1

    
if (menor == 0):
    print ("Sem valores no intervalo definido.")
else:
    print ("O menor valor no intervalo vale %.2f."%(menor))