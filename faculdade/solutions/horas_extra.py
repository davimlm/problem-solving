# A jornada de trabalho semanal de um funcionário é de 40 horas. Se o funcionário trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50% (o acréscimo de 50% ocorre somente sobre as horas que excederem às 40 horas semanais). Escreva um programa que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas. Considere que o mês possua 4 semanas exatas.

# A saída do programa deve ser: "O salário total do funcionário é R$ S.", sendo S o salário em reais, mostrado com duas casas decimais.

horas_mes = int(input())
salario_hora = float(input())

if (horas_mes > 160):
    horas_extra = horas_mes - 160
    salario = ((horas_mes - horas_extra)*salario_hora) + ((horas_extra*salario_hora)*1.5)
    print ("O salário total do funcionário é R$ {:.2f}.".format(salario))
else:
    salario = (horas_mes*salario_hora)
    print ("O salário total do funcionário é R$ {:.2f}.".format(salario))