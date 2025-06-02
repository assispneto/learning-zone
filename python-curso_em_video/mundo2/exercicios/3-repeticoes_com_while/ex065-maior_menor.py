# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print('\n')
n       = ''
soma    = 0

entrada = float(input('Digite um número > '))
maior   = entrada
menor   = entrada
cont    = 1
soma    = (soma+entrada)

n       = str(input('Deseja continuar [S/N]? > ')).strip()[0]
if (n in 'Nn'):
    print('[TOTAL DE VALORES]   -> {}'.format(cont))
    print('[MEDIA]              -> {}'.format(entrada))
    print('[MAIOR VALOR]        -> {}'.format(maior))
    print('[MENOR VALOR]        -> {}'.format(menor))
else:
    while (n in 'Ss'):
        entrada = float(input('Digite um número > '))
        n       = str(input('Deseja continuar [S/N]? > ')).strip()[0]
        # Total de valores
        cont = cont+1
        # Media
        soma = (entrada+soma)
        # Maior valor
        if entrada>maior:
            maior=entrada
        if entrada<menor:
            menor=entrada
    media  = (soma/cont)
    print('[TOTAL DE VALORES]   -> {}'.format(cont))
    print('[MEDIA]              -> {:.1f}'.format(media))
    print('[MAIOR VALOR]        -> {:.1f}'.format(maior))
    print('[MENOR VALOR]        -> {:.1f}'.format(menor))
    

