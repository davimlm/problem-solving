# A biblioteca de uma escola adota um sistema de multas para disciplinar a administração dos empréstimos, dependendo da quantidade de dias de atraso para cada livro. Assim, a multa é calculada, em função dos dias de atraso, da seguinte maneira:

# até 1 dia:                      R$ 1.00, independentemente da quantidade de livros;
# de 2 até 5 dias:            R$ 2.00 por dia e por livro em atraso;
# de 6 até 10 dias:          R$ 3.00 por dia e por livro em atraso;
# de 11 até 29 dias:        R$ 4.00 por dia e por livro em atraso;
# mais que 29 dias:        R$ 4.00 por dia e por livro em atraso, mais taxa de R$ 50,00.
# Sua função é implementar um programa para facilitar o gerenciamento das multas da biblioteca. As entradas são o número de dias e a quantidade de livros em atraso. Se não houver atraso (número de dias de atraso igual a zero), o programa deve emitir a mensagem: "Devolução no prazo.". Com atraso (número de dias de atraso maior que zero), a mensagem será: "Multa por atraso de R$ X.", em que X é o valor da multa, mostrado com duas casas decimais.

# Exemplo de entrada:
# 1
# 2

# Exemplo de saída:
# Multa por atraso de R$ 1.00.

dias = int(input())                                                
livros = int(input())

if dias > 0:
    if (dias == 1):
        multa = 1
    
    elif (dias >= 1 and dias <= 5):
        multa = (dias*2)*livros
    
    elif (dias >= 6 and dias <= 10):
        multa = (dias*3)*livros

    elif (dias >= 11 and dias <= 29):
        multa = (dias*4)*livros

    elif (dias > 29):
        multa = ((dias*4)*livros) + 50
    
    print ("Multa por atraso de R$ %.2f."%(multa))
    
else: 
    print ("Devolução no prazo.")