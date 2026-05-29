# Implementar um algoritmo que faça a leitura de um determinado valor e verifique se o valor é diferente de zero. Se sim, deve-se imprimir "É diferente!"". Caso contrário, a seguinte frase deve ser impressa: "É zero!".
 
# Os seguintes testes serão realizados:

# ENTRADA 1:
# 3
# SAÍDA 1:
# É diferente!

# ENTRADA 2:
# 0
# SAÍDA 2:
# É zero!

numero = float(input())

if (numero == 0):
    print("É zero!")
else:
    print("É diferente!")