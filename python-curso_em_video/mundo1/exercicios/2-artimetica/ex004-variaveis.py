# Programa que leia algo pelo teclado e mostre na tela seu tipo
# primitivo e todas as informacoes possiveis sobre ele


conteudo = input('\nDigite qualquer coisa: ')

# Para descobrir o tipo primitivo:
# print('O tipo primitivo desse conteudo eh: ', type(conteudo))

print('\nAS SEGUINTES INFORMAÇÕES FORAM ENCONTRADAS:')

print('-> Alfabetico: ', conteudo.isalpha())
print('-> Numerico: ',conteudo.isalnum())
print('-> Alfanumerico: ',conteudo.isalnum())
print('-> Ascii: ', conteudo.isascii())
print('-> Digit: ', conteudo.isdigit())
print('-> Lower: ', conteudo.islower())
print('-> Identifier: ', conteudo.isidentifier())

print('-> Só tem espaços: ', conteudo.isspace())
print('-> Esta capitalizada: ', conteudo.istitle())     # Não esta em maisculas nem em minusculas

