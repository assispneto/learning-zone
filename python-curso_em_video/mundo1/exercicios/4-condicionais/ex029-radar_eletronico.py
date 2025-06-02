# Programa que ler a velocidade de um carro. Se ele ultrapassar
# 80Km/h, mostra uma mensagem dizendo que ele foi multado.
# OBS -> A multa vai custar R$7,00 por cada Km acima do limite.


velocidade  = int(input('Qual velocidade o carro estava? '))

if velocidade <= 80:
    print('O motorista não foi multado')
else:
    print('O motorista foi multado e deverá pagar R${}'.format((velocidade-80)*7))


