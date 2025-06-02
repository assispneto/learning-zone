# Reajuste salarial

salario = float(input('Qual seu salário atual? R$ '))
reajuste    = (salario * (15/100))
salarioFinal  = (salario+reajuste)

print('O salário com um aumento de 15%, passa a ser de R${:.2f}'.format(salarioFinal))


