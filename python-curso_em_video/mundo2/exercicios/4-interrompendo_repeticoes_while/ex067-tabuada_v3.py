# Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

print('\n>----------- TABUADA -----------<')
print('> OBS: -1 encerra sua tabuada <\n')

counter = 0
while True:
    valor = int(input('Digite um valor > '))
    if (valor==-1):
        print('##### PROGRAMA ENCERRADO #####')
        break
    else:
        print('---------------')
        print(f'-> TABUADA DE {valor} ')
        while counter<=10:
            print(f'{valor:2} X {counter:2} = {valor*counter:2}')
            counter = counter+1
        print('---------------')
    counter = 0


