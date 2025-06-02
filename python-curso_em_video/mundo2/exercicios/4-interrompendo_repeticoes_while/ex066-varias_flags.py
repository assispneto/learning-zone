# Crie um programa que leia números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

counter = 0
soma    = 0

while True:
    valor = int(input('Digite um numero > '))
    if (valor == 999):
        break
    soma    = (soma+valor)
    counter = counter+1
print(f'     [Soma dos valores]: {soma}')
print(f'[Quantidade de valores]: {counter}')


