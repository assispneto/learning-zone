# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1      = int(input('Primeiro valor > '))
n2      = int(input('Segundo valor > '))
checar  = 0

while (checar==0):
    print('''\nQUAL OPERAÇÃO VOCÊ DESJA REALIZAR:')
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')

    op = int(input(' > '))
    if op==1:
        print('\n--> Soma: {}'.format(n1+n2))
    elif op==2:
        print('\n--> Multiplicação: {}'.format(n1*n2))
    elif op==3:
        if n1>n2:
            maior=n1
            print('--> O maior é {}'.format(maior))
        if n1==n2:
            print('\n--> Os valores são iguais')
        else:
            print('--> O maior é {}'.format(maior))
            maior=n2
    elif op==4:
        n1  = int(input('--> Primeiro valor > '))
        n2  = int(input('--> Segundo valor > '))
    elif op==5:
        checar=1
    else:
        print('## OPÇÃO INVÁLIDA ##')
print('---------Programa encerrado---------')


