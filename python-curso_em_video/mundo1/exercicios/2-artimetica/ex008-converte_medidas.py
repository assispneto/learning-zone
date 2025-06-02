# Conversor de medidas


valor = int((input('Digite uma distância (em metros): ')))

km  = (valor/1000)
hm  = (valor/100)
dam = (valor/10)
dm  = (valor*10)
cm  = (valor*100)
mm  = (valor*1000)

print('O valor da distancia de {}m será: '.format(valor))
print(' -> {}km\n -> {}hm\n -> {}dam\n -> {}dm\n -> {}cm\n -> {}mm'.format(km,hm, dam, dm, cm, mm))


