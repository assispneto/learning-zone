# Faça um programa que calcule a soma entre todos os números ímapares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500

soma    = 0
count   = 0

for c in range(1, 501, 2):
    if c%3 == 0:
        soma  = soma+c
        count = count+1
print('Ao todo foram {} valores, e sua soma é {}'.format(count, soma))


