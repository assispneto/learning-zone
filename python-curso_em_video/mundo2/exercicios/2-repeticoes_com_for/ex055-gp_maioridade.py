# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

anoAtual        = datetime.date.today().year
contMaiorIdade  = 0
contMenorIdade  = 0
idade           = 0

for pessoa in range(1, 8):
    anoNascimento = int(input('Digite o ano de nascimento da {}ª pessoa > '.format(pessoa)))
    idade = anoAtual-anoNascimento
    if idade >= 21:
        contMaiorIdade += 1
    else:
        contMenorIdade += 1

print(' -> {} pessoas possuem a maioridade!'.format(contMaiorIdade))
print(' -> {} pessoas são menores de idade!'.format(contMenorIdade))


