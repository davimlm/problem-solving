# Faça um programa, usando a estrutura de repetição while, para fazer a validação de e-mail usando confirmação. Para tanto, seu programa deve ler um e-mail e sua respectiva confirmação de senha. Caso o e-mail digitado e a confirmação sejam diferentes, o programa deve emitir a mensagem de erro "Confirmação falhou!" e novamente solicitar um e-mail e sua confirmação até que sejam iguais. No caso da confirmação ser bem sucedida, o programa deve emitir uma mensagem "E-mail confirmado!"

# A seguir, exemplos de testes que serão realizados:  

# Teste 1:
# meuemail@meuservidor.com
# meuEmail@meuservidor.com
# Confirmação falhou!

# Teste 2:
# meuemail@meuservidor.com
# meuemail@meuservidor.com
# E-mail confirmado!

email = str(input()) 
confirmaEmail = str(input()) 

while(email != confirmaEmail):
    print("Confirmação falhou!")
    email = str(input()) 
    confirmaEmail = str(input()) 
print("E-mail confirmado!")