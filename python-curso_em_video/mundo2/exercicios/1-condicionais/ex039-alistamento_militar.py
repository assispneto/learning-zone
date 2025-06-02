# Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo


from datetime import date

anoNascimento = int(input('Em qual ano você nasceu? '))

anoAtual    = date.today().year
idade       = (anoAtual-anoNascimento)

if idade==18:
    print('Você tem {}, portanto deve se alistar!'.format(idade))

elif idade<18:
    saldo   = (18-idade)
    print('Daqui há {} anos você deve se alistar'.format(saldo))

else:
    saldo   = (idade-18)
    print('Você deveria ter se alistado há {} anos'.format(saldo))


