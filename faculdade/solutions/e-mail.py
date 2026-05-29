# Escreva um programa que leia o endereço de e-mail do remetente, o endereço de e-mail do destinatário e o texto da mensagem. Após isso, imprima o e-mail no seguinte formato:
# De:<endereço remetente>
# Para:<endereço destinatário>
# Mensagem:<texto da mensagem>

# Exemplo:
# # De:funcionario@empresa.com
# Para:gerente@empresa.com
# Mensagem:Segue relatorio de vendas desta semana.

# Entrada:
# endereço de e-mail do remetente
# endereço de e-mail do destinatário
# texto da mensagem

# Saída:
# e-mail formatado conforme enunciado

remetente = str(input())
destinatario = str(input())
mensagem = str(input())

print ("De:%s" % remetente)
print ("Para:%s" % (destinatario))
print ("Mensagem:%s" % mensagem)