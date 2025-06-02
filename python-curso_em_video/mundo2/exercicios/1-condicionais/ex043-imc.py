# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# –> IMC abaixo de 18,5: Abaixo do Peso
# –> Entre 18,5 e 25: Peso Ideal
# –> 25 até 30: Sobrepeso
# –> 30 até 40: Obesidade
# –> Acima de 40: Obesidade Mórbida


print('Informe os seguintes dados para calcularmos seu IMC: ')

peso = float(input('Peso (em kg): '))
altura = float(input('Altura: '))

imc = (peso/(altura*altura))
print('Seu IMC é {:.2f}, logo: '.format(imc))

if imc<18.5:
  print('Você está abaixo do peso ideal')
  
elif imc>=18.5 and imc<25:
  print('Você está no peso ideal!')
  
elif imc>=25 and imc<35:
  print('Você está no sobrepeso!')
  
elif imc>=35 and imc<40:
  print('Você está no estado de obesidade!')
  
else:
  print('Você está em obesidade mórbida!')


