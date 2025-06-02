# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado


valorCasa = (float(input('Qual o valor da casa? ')))
salario   = (float(input('Qual seu salário? ')))
anos      = (float(input('Em quantos anos você vai pagar? '))) 

limiteSalario   = ((30/100)*salario)    # 30% do salario
tempoMeses      = (anos*12)
valorPrestacao  = (valorCasa/tempoMeses)

print('-'*35)

if valorPrestacao<limiteSalario:
  print('O valor da prestação: R${:.2f}'.format(valorPrestacao))
  print('30% do seu salário: R${}'.format(limiteSalario))
  print('Status: ACEITO')
  
elif valorPrestacao>limiteSalario:
  print('O valor da prestação: R${:.2f}'.format(valorPrestacao))
  print('30% do seu salário: R${}'.format(limiteSalario))
  print('Status: NEGADO')


