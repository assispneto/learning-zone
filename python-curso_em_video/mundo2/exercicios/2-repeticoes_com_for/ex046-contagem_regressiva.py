# Faça um programa que mostre na tela uma contagem regressiva para o estouro de 
# fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time
import os 

print('\nOBS: Apenas execute esse progrma se não tiver animais por perto!!')
print('Em 10s os fogos irão estourar...')

for c in range(10, 0, -1):
    print(c)
    time.sleep(1)

os.system('cls') or None 

print('******************************* (imagine aqui uma explosão)')


