# Tinta necessária para pintar uma parede

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

areaParede = (largura*altura)
tinta = (areaParede/2)   # A cada 2 quadrados, 1l de tinta é necessário

print('Sua parede tem a dimensão {}x{}, sendo sua área {}m²'.format(largura, altura, areaParede))
print('Para pintar, serão necessários {}l de tinta'.format(tinta))


