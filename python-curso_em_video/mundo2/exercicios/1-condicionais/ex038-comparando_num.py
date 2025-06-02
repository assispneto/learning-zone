# Escreva um programa que leia dois números inteiros e compare-os


valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

if valor1>valor2:
  print('{} é maior que {}'.format(valor1, valor2))
 
elif valor2>valor1:
  print('{} é maior que {}'.format(valor2, valor1))
  
else:
  print('Os dois são iguais!')


