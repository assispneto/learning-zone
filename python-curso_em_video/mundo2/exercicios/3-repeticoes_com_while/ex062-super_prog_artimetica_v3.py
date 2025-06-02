# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

# FORMULA: an = a1+(n-1)*r

# --------------------------- Lógica Prof. Guanabara ---------------------------

primeiroTermo   = int(input('PRIMEIRO TERM0: '))
razao           = int(input('RAZAO: '))

termo           = primeiroTermo
cont            = 1
total           = 0
mais            = 10

while (mais!=0):
    total = (total+mais)
    while (cont<=total):
        print('{} -> '.format(termo), end='')
        termo   = (termo+razao)
        cont    = cont+1
    print('PAUSA')
    mais = (int(input('Você deseja ver mais quantos valores dessa sequência > ')))
print('Tivemos ao todo {} termos'.format(total))


