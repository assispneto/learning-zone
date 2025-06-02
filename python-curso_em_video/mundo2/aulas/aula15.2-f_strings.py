####################### F-String #######################
# -> Forma de usar o print mostrando o valor da variável

variavel1 = 'VARIAVEL1'
variavel2 = 'VARIAVEL2'

# Python 2
# print('>--------- Print 1 ---------<')
# print('[VALOR 1]: %s; [VALOR 2]: %d'%(variavel1, variavel2))
# Python 3
print('>--------- Print 2 ---------<')
print('[VALOR 1]: {}; [VALOR 2]: {}'.format(variavel1, variavel2))
# Python 3.6+
print('>--------- Print 3 ---------<')
print(f'[VALOR 1]: {variavel1}; [VALOR 2]: {variavel2}')


