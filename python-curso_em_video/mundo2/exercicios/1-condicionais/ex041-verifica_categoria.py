# A Confederação Nacional de Natação precisa de um programa que leia o 
# ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# –> Até 9 anos: MIRIM
# –> Até 14 anos: INFANTIL
# –> Até 19 anos: JÚNIOR
# –> Até 25 anos: SÊNIOR
# –> Acima de 25 anos: MASTER


idade = int(input('Digite sua idade e informaremos a categoria para competições nacionais de natação: '))

if idade<=9:
  print('Você se encaixa na categoria MIRIM!')
elif idade<=14:
  print('Você se encaixa na categoria INFANTIL!')
elif idade<=19:
  print('Você se encaixa na categoria JUNIOR!')
elif idade<=20:
  print('Você se encaixa na categoria SÊNIOR')
else:
  print('Você se encaixa na categoria MASTER!')


