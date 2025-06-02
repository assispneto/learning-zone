# Programa que informa o DOBRO, o TRIPLO e a RAIZ QUADRADA


valor = int(input('\nDigite um numero: '))

d   = (valor*2)
t   = (valor*3)
sqr = (valor ** (1/2))

print('\nO dobro de {} é:         {}'.format(valor, d))
print('O triplo de {} é:          {}'.format(valor, t))
print('a raiz quadrada de {} é:   {}'.format(valor, sqr))


