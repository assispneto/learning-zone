# Recebe um numero do usuario e logo após informa seu antecessor e seu sucessor

# PRIMEIRA FORMA
valor = int(input('Digite um numero: '))

antecessor = valor-1
sucessor   = valor+1

print('\nPRIMEIRA FORMA: utilizando tres variaveis')
print('Seu antecessor é: {}'.format(antecessor))
print('Seu sucessor é: {}'.format(sucessor))

# SEGUNDA FORMA
print('\nSEGUNDA FORMA: manipulando apenas uma variavel')
print('Analisando o numero {}, seu antecessor é {} e seu sucessor {}'.format(valor, (valor-1), (valor+1)))


