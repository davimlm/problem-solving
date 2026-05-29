# Escreva um programa, usando a estrutura de repetição while, para ler N valores reais e determinar quantos destes estão no intervalo fechado [10, 20]. Seu programa deve receber primeiramente o valor N.

# A saída do programa deve ser: "Tem v valores no intervalo [10,20].", em que v é a quantidade de valores encontrada.

valorN = int(input())
n = 0
contador = 0

while (n < valorN):
    valor = float(input())
    n = n + 1
    if(valor <= 20 and valor >= 10):
        contador = contador + 1
    
    
    
print("Tem", contador,  "valores no intervalo [10,20].")