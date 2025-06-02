# Programa que ler o comprimento de três retas e informa ao usuário se elas podem ou não formar um triângulo

# OBS (preparaenem.com) -> sempre que a soma das medidas dos segmentos que estão sendo
# girados for maior que a medida do terceiro segmento, é possível construir um triângulo.
# Tendo: a + b < c,     a + c < b,       b + c < c

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

condicao1   = (seg1+seg2 < seg3)
condicao2   = (seg1+seg3 < seg2)
condicao3   = (seg2+seg3 < seg1)

if condicao1 and condicao2 and condicao3:
    print('É possível formar um triângulo com esses segmentos!')
else:
    print('Não é possível formar um triângulo com esses segmentos!')


