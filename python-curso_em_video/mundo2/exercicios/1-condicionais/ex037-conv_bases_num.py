# Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.


valor = int(input('Digite um número: '))

print('Dadas as opções: ')
print('1 - BINÁRIO')
print('2 - OCTAL')
print('3 - HEXADECIMAL')
op = int(input('Você deseja converter {} para qual base de conversão? '.format(valor)))

if op==1:
    print('{} em binário é {}'.format(valor, (bin(valor))))

elif op==2:
    print('{} em binário é {}'.format(valor, (oct(valor))))

elif op==3:
    print('{} em binário é {}'.format(valor, (hex(valor))))

else:
    print('Opção inválida, tente novamente')


