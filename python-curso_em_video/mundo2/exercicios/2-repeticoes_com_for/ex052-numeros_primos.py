# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

valor   = int(input('Digite um numero > '))
cont    = 0

for c in range (1, valor+1):
    if valor%c == 0:
        cont = cont+1

if cont == 2:
    print('Esse número é primo!')
else:
    print('Esse número NÃO é primo!')

########## RESOLUÇÃO GUANABARA ##########
for c in range (1, valor+1):
    if valor%c == 0:
        print('\033[34m', end=' ')
    else:
        print('\033[33m', end=' ')
    print('{} '.format(c), end='')


