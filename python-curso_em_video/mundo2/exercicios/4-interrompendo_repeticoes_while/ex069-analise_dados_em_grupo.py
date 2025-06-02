# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# ----> A) quantas pessoas tem mais de 18 anos.
# ----> B) quantos homens foram cadastrados.
# ----> C) quantas mulheres tem menos de 20 anos.

idade               = 0
sexo                = ''
n                   = ''
maioresIdade        = 0
homens              = 0
mulheresMenosDe20   = 0

while True:
    print('\n##### CADASTRO DE PESSOA #####')
    idade   = int(input('--> Idade  > '))
    sexo    = str(input('--> Sexo [M/F]> ')).strip().lower()[0]
    while sexo not in 'mf':
        print('# Digite M para sexo maculino e F para feminino')
        sexo = str(input('--> Sexo [M/F]> ')).strip().lower()[0]
    n = str((input('--> Deseja continuar [S/N]? > '))).strip().lower()[0]
    if idade>18:
        maioresIdade = maioresIdade+1
    if sexo == 'm':
        homens = homens+1
    if (idade<20) and (sexo =='f'):
        mulheresMenosDe20 = mulheresMenosDe20+1
    if n in 'n':
        break
print('##### RELATORIO GERAL #####')
print(f'# Pesoas com mais de 18 anos:   {maioresIdade}')
print(f'# Mulheres com menos de 20anos: {mulheresMenosDe20}')
print(f'# Total de homens:              {homens}')


