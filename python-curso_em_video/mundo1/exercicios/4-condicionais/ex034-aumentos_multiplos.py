# Programa que pergunta o salário de um funcionário e calcula o valor do seu aumento.
# -> Para salários superiores a R$1250,00, aumento de 10%
# -> Para os inferiores ou iguais, aumento de 15%

salario     = float(input('Qual seu salário? R$'))
aumento1    = ((10/100)*salario)
aumento2    = ((15/100)*salario)

if salario>1250.00:
    print('Com o aumento de R${:.2f}, seu novo salário será R${:.2f}'.format(aumento1, aumento1+salario))

if salario<=1250.00:
    print('Com o aumento de R${:.2f}, seu novo salário será R${:.2f}'.format(aumento2, aumento2+salario))


