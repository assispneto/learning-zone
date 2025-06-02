# Programa que ler um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

valor = int(input('Digite um número de 0 a 999: '))

unidade = ((valor // 1)    % 10)    # Divisão inteira por 1 e depois tiro o módulo por 10
dezena  = ((valor // 10)   % 10)    # Divisão inteira por 10 e depois tiro o módulo por 10
centena = ((valor // 100)  % 10)    # Divisão inteira por 100 e depois tiro o módulo por 10
uMilhar = ((valor // 1000) % 10)    # Divisão inteira por 1000 e depois tiro o módulo por 10

print('Analisando seu número:')
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, uMilhar))


