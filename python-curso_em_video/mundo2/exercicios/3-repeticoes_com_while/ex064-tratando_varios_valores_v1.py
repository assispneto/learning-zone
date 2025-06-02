# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag). 

entrada = cont = soma = 0

print('\n')
while (entrada!=999):
    entrada = (int(input('Digite um número [999 para o programa] > ')))
    if (entrada!=999):
        soma    = (entrada+soma)
        cont    += 1
print('>>>> Foram digitados [{}] números. A soma entre eles é [{}]'.format(cont, soma))


################################ Resolução Guanabara ################################
# entrada = cont = soma = 0
# entrada = (int(input('Digite um número [999 para o programa] > ')))
# while entrada!=999:
#    soma    = (entrada+soma)
#    cont    += 1
#    entrada = (int(input('Digite um número [999 para o programa] > ')))


