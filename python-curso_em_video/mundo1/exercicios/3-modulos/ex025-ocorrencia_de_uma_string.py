# Programa que ler o nome de uma pessoa e diga se ela tem “SILVA” no nome

nome        = str(input('Qual seu nome completo? ')).strip()
condicao    = nome.lower() in 'silva'

print('Seu nome tem silva? {}'.format(condicao))


