# Acertar um numero aleatorio gerado pelo computador

import random

valorAleatorio  = random.randint(1, 5)
valorEscolhido  = int(input("\nPense em um número entre 1 e 5 e irei tentar adivinhar: "))
print('='*60)

if valorEscolhido == valorAleatorio:
    print('\nVocê venceu :)')
else:
    print('\nVocê perdeu. O numero escolhido foi {} :('.format(valorAleatorio))


