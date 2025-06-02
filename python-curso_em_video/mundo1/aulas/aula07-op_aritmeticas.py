#################### Operacoes aritmeticas ####################


# Operadores:
# +  -> Soma
# -  -> Subtracao
# *  -> Multiplicacao
# /  -> Divisao
# ** -> Exponenciacao
# '//' -> Divisao inteira (nao mostra depois da virgula)
# %  -> Resto da divisao (mostra o que sobra sem a divisao usando virgula)

# =  -> Atribuo que uma coisa eh igual a outra
# == -> Comparo de dois elementos sao iguais

# Ordem de procedencia:
# ()  ->  **  ->  * / // %  ->  + -

# Alinhamento:
valor = input('Digite algo: ')
print('Valor em 20 caracteres:                  |{:20}|...fim'.format(valor))
print('Alinhamento a direita:                   |{:>20}|...fim'.format(valor))
print('Alinhamento a esquerda:                  |{:<20}|...fim'.format(valor))
print('Alinhamento ao centro:                   |{:^20}|...fim'.format(valor))
print('Alinhamento ao centro com "+" em volta:  |{:+^20}|...fim'.format(valor))
print('\n')

# Usando o print para somar:
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
print('O resultado da soma é: {}'.format(n1+n2))    # Recomendado usar quando eu nao precisar do valor em outro momento
print('\n')

# Usando os operadores:
soma        = n1+n2
subtracao   = n1-n2
mult        = n1*n2
div         = n1/n2
div_i       = n1//n2
pot         = n1**n2

print('Soma: {}'.format(soma))                      # end=' ' -> serve para nao pular pra outra linha com o print
print('Subtração: {}'.format(subtracao))
print('Multiplicação: {}'.format(mult))

print('Divisão: {}'.format(div))
print('Divisão para 3 casas decimais: {:.3f}'.format(div))

print('Divisão Inteira: {}'.format(div_i))
print('Potência: {}'.format(pot))


