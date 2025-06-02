# Aluguel de carros

dias        = int(input('Quantos dias vc utilizou o carro? '))
distancia   = float(input('Quantos km rodados? '))

valorFinal  = ((dias*60) + (0.15*distancia))

print('O total a pagar é: R${}'.format(valorFinal))


