# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# –> à vista dinheiro/cheque:   10% de desconto
# –> à vista no cartão:         5% de desconto
# –> em até 2x no cartão:       preço formal 
# –> 3x ou mais no cartão:      20% de juros


print('Simulando sua compra...')
valor = float(input('Qual o valor total do produto? R$\n'))

print('Temos as seguintes opções de pagamento: ')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] vista no cartão')
print('[ 3 ] em até 2x no cartão')
print('[ 4 ] 3x ou mais no cartão ')
opcaoPag = int(input('\nQual a opção de pagamento? '))

op1 = ( valor - ((10/100)*valor) )
op2 = ( valor - ((5/100)*valor) )
op3 = valor
op4 = ( valor + ((20/100)*valor) )

if opcaoPag==1:
  print('O valor final será de R${}'.format(op1))
elif opcaoPag==2:
  print('O valor final será de R${}'.format(op2))
elif opcaoPag==3:
  print('O valor final será de R${}'.format(op3))
elif opcaoPag==4:
  print('O valor final será de R${}'.format(op4))


