# Programa que ler o comprimento de três retas e informa ao usuário se elas 
# podem ou não formar um triângulo, mostrando também qual o tipo desse triângulo
# OBS (preparaenem.com) -> sempre que a soma das medidas dos segmentos que estão sendo
# girados for maior que a medida do terceiro segmento, é possível construir um triângulo.
# Tendo: a + b < c,     a + c < b,       b + c < c


# Obtendo as medidas dos segmentos
seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

# Verificando sua classificação
# equilatero  = (seg1==seg2==seg3)
# isosceles   = ((seg1==seg2) or (seg1==seg3) or (seg2==seg3))
# escaleno    = (seg1!=seg2!=seg3)

if ((seg1<seg2+seg3) and (seg2<seg1+seg3) and (seg3 < seg1+seg2)):
    print('É possível formar um triângulo com esses segmentos.')
    if seg1 == seg1 == seg3:
        print('Ele será um TRIÂNGULO EQUILÁTERO')
    elif seg1 != seg2 != seg3 != seg1:
        print('Ele será um TRIÂNGULO ESCALENO')
    else:
        print('Ele será um TRIÂNGULO ISOSCELES')
else:
    print('Não é possível formar um triângulo com esses segmentos!')


