# Programa que recebe a distância de uma viagem em km e em seguida
# calcula o preço da passagem, cobrando R$0,50 por km para viagens
# de até 200Km e R$0,45 para viagens mais longas.

distancia   = float(input('Digite a distância da sua viagem: '))
if distancia <= 200:
    print('O preço da passagem será de: R${:.2f}'.format(distancia*0.50))
else:
    print('O preço da passagem será de: R${:.2f}'.format(distancia*0.45))


