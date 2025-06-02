# Seno, cosseno e tangente

import math
angulo = float(input('Digite o ângulo: '))
radiano = math.radians(angulo)  # Convertendo para radiano

seno     = math.sin(radiano)
cosseno  = math.cos(radiano)
tangente = math.tan(radiano)

print('Seno: {:.3f}\nCosseno: {:.3f}\nTangente: {:.3f}'.format(seno, cosseno, tangente))


