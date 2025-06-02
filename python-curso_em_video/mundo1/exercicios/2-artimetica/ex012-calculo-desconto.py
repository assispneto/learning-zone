# Calculando descontos

valor = float(input('Qual o preço do produto? R$ '))
desconto    = (valor * (5/100))
valorFinal  = (valor-desconto)

print('O produto com um desconto de 5%, irá custar: R${:.2f}'.format(valorFinal))


