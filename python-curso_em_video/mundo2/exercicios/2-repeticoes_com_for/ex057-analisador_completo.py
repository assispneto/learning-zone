# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: 
# -> média de idade do grupo;
# -> qual é o nome do homem mais velho; 
# -> quantas mulheres têm menos de 20 anos.

media           = 0
auxIdade        = 0
nomeMaisVei     = ''
mulherMaisDe20  = 0
maiorIdade      = 0
print('\n')

for pessoa in range(1,5):
    print('################ {}ª PESSOA ################'.format(pessoa))
    nome    = str(input('NOME > '))
    idade   = int(input('IDADE > '))
    sexo    = str(input('SEXO (M/F) > '))

    # MEDIA DE IDADE
    auxIdade = (idade + auxIdade)

    # NOME HOMI MAIS VELHO
    if ((pessoa==1) and (sexo in 'Mm')):
        nomeMaisVei = nome
        maiorIdade  = idade
    else:
        if idade>maiorIdade:
            nomeMaisVei = nome

    # MULHER COM MENOS DE 20
    if ((sexo in 'Ff') and (idade<20)):
        mulherMaisDe20 += 1

# Media
media = (auxIdade/4)

# Mostrando os dados
print('\n')
print('---> MEDIA DE IDADE DO GRUPO: {}'.format(media))
print('---> HOMEm MAIS VELHO: {}'.format(nomeMaisVei))
print('---> TOTAL DE MULHERES COM MENOS DE 2O ANOS: {}'.format(mulherMaisDe20))


