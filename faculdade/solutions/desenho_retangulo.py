# Escreva um programa que desenhe um retângulo composto de x (x > 2) linhas e y colunas (y > 2), no qual o perímetro é composto por um símbolo "+". 

# Como exemplo, se x = 3 e y = 7, seu programa deve desenhar o seguinte:

# +++++++
# +           +
# +++++++

# Caso x ou y esteja fora dos padrões o programa deve emitir uma mensagem de erro: "Dimensões fora das especificações.".

# Não é permitido usar listas ou arrays do Python, ou de qualquer de suas bibliotecas.

x = int(input())
y = int(input())

if (x <= 2 or y <= 2):
    print("Dimensões fora das especificações.")

else: 
    for i in range (x):
        for j in range (y):
            if ((i == 0 or i == x - 1) or (j == 0 or j == y - 1)):
                print("+", end = "")
            else:
                print (" ", end= "")
        print("")