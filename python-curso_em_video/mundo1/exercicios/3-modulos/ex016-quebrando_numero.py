# Ler um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira

# Primeira forma:
import math
num = float(input('Digite um valor: '))
print('Valor digitado: {}'.format(num))
print('Sua porção inteira é: {}'.format(math.trunc(num)))

# Segunda forma:
print('Valor digitado: {}'.format(num))
print('Sua porção inteira é: {}'.format(int(num)))


