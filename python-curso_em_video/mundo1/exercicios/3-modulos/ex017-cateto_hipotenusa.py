# Ler o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

# Primeira forma:
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hip = (((co ** 2) + (ca ** 2)) ** (1/2))
print('A hipotenusa1 vale: {:.2f}'.format(hip))

# Segunda forma:
from math import hypot
hi = math.hypot(co, ca)
print('A hipotenusa2 vale: {:.2f}'.format(hi))


