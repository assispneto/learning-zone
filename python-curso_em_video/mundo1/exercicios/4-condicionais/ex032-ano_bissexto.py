# Programa que ler um ano qualquer e mostra se ele é bissexto.
# OBS -> Digitando '0' o programa analisa o ano atual (hoje ta sendo 2023)

from datetime import date

ano = int(input("Digite o ano: "))

if ano == 0:
    ano = date.today().year

if (ano%4 == 0) and (ano%100 !=0) or (ano%400 == 0):
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))


