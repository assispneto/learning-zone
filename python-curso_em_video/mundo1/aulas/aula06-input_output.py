#################### Tipos primitivos e entrada e saida de dados ####################


# Eh importante colocar o 'int' antes do input para o programa entender que se trata de um numero inteiro
# O input eh interpretado como uma string, caso eu nao tivesse colocar o 'int' ele entenderia os numeros como strings

valor1 = int(input('Digite seu numero: '))
valor2 = int(input('Digite outro numero: '))

s = valor1+valor2

print('\n')

# Forma chata de dar print:
print('A soma entre',valor1, 'e',valor2, 'vale:', s, '   (print 1)')

# Forma prática e legal:
print('A soma entre {} e {} vale: {}   (print 2)'.format(valor1, valor2, s))


