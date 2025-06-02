# Faça um programa que leia um número qualquer e mostre o seu fatorial. 
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

# ---> Usando a biblioteca:
# from math import factorial
# f = factorial(valor_recebido)

valor       = int(input('Digite um número e descubra seu fatorial > '))
valorAux    = valor
fatorial    = 1

while (valorAux!=0):
    print('{}'.format(valorAux), end='')
    print(' x ' if valorAux>1 else ' = ', end='')
    fatorial    = valorAux*fatorial
    valorAux    = valorAux-1
print('{}'.format(fatorial))


