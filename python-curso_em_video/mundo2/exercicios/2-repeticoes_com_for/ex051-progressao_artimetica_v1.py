# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

# FORMULA: an = a1+(n-1)*r

primeiroTermo   = int(input('PRIMEIRO TERM0: '))
razao           = int(input('RAZAO: '))
decimo          = primeiroTermo + (10-1) * razao

for c in range(primeiroTermo, decimo, razao):
    print('{}'.format(c), end=' -> ')

print('FIM')


