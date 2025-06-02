# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

import random

valorAleatorio  = random.randint(1, 100)
valorEscolhido  = int(input("\nPense em um número entre 1 e 100 > "))
contTenativas   = 0

while (valorEscolhido!=valorAleatorio):
    if(valorEscolhido>valorAleatorio):
        print('==== Mais baixo ====')
        valorEscolhido  = int(input("Tente novamente > "))
    else:
        print('==== Mais alto ====')
        valorEscolhido  = int(input("Tente novamente > "))
    contTenativas += 1
print('-------------------------')
print('Depois de {} tentativas,'.format(contTenativas))
print('finalmente você venceu!!')
print('-------------------------')


