#################### Utilizando módulos ####################

# 'import ctrl+espaço' -> lista as bibliotecas que posso usar (as disponíveis no meu pc)
# Python Package Index -> módulos que programadores disponibilizam para a comunidades (bibliotecas extras)

# BIBLIOTECA MATH
import math             # Importando toda a biblioteca math
#from math import sqrt   # Importando apenas um método da biblioteca


print('\nBIBLIOTECA MATH')
valor   = int(input('Digite um numero: '))
raiz    = math.sqrt(valor)      # sqrt -> raiz quadrada

print('Resultado da raiz quadrada: {}'.format(raiz))


# BIBLIOTECA RANDOM
print('\nBIBLIOTECA RANDOM')
import random           # Biblioteca para gerar números aleatórios

num  = random.random()
print('O numero aleatório é: {}'.format(num))

num2 = random.randint(1, 100)        # Numero aleatorio inteiro de 1 até 10
print('O numero aleatório entre 1 e 10 é: {}'.format(num2))


# BIBLIOTECA EMOJI (extra)
# import emoji
# print(emoji.emojize("Olá :sunglasses:", use_aliases=True))


