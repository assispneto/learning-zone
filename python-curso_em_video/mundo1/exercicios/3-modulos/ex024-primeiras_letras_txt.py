# Programa que ler o nome de uma cidade diga se ela começa ou não com o nome “SANTO”

cidade      = str(input('Qual sua cidade? ')).strip()
condicao    = (cidade[:5].lower() == 'santo')

print(condicao)


