# A prefeitura de uma cidade abriu uma linha de crédito para os funcionários estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário bruto. Implemente um algoritmo que leia o salário bruto e o valor da prestação e informe se o empréstimo pode ("Empréstimo Liberado!") ou não ("Empréstimo Negado!") ser concedido.
 
# Os seguintes testes serão realizados,   

# ENTRADAS 1:
# 1000
# 400
# SAÍDA 1:
# Empréstimo Negado!


# ENTRADAS 2:
# 3000
# 500
# SAÍDA 2:
# Empréstimo Liberado!

# ENTRADAS 3:
# 6000
# 1800
# SAÍDA 2:
# Empréstimo Liberado!

salarioBruto = float(input())
prestacao = float(input())

if (prestacao > (salarioBruto*0.3)):
    print("Empréstimo Negado!")
else:
    print("Empréstimo Liberado!")