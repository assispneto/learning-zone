# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while

# FORMULA: an = a1+(n-1)*r

primeiroTermo   = int(input('PRIMEIRO TERM0: '))
razao           = int(input('RAZAO: '))
cont            = 0
pa              = 0

while (cont!=10):
    print('{}'.format(pa), end=' -> ')
    pa = (primeiroTermo+razao)
    primeiroTermo = pa
    cont = cont+1
print('FIM')


