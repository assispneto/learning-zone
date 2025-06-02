# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0

for c in range(1, 7):
    valor = int(input('Digite o valor {}: '.format(c)))
    if valor%2 == 0:
        soma = soma+valor
        cont = cont+1

print('Tivemos ao todo {} números pares.\nA soma dos números pares digitados é: {}'.format(cont, soma))


