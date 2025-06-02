# Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos

maiorPeso   = 0
menorPeso   = 0
aux         = 0

for pessoa in range(1,6):
    peso    = float(input('Digite o peso da {}ª pessoa > '.format(pessoa)))
    if (pessoa==1):
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso>maiorPeso:
            maiorPeso=peso
        if peso<menorPeso:
            menorPeso=peso

print('-> MAIOR peso: {:.2f}kg'.format(maiorPeso))
print('-> MENOR peso: {:.2f}kg'.format(menorPeso))


