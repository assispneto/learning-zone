# Programa que leia algo pelo teclado e mostre na tela seu tipo
# primitivo e todas as informacoes possiveis sobre ele

conteudo = input('\nDigite qualquer coisa: ')

print('\nAS SEGUINTES INFORMAÇÕES FORAM ENCONTRADAS:')

print('-> Alfabetico: ', conteudo.isalpha())
print('-> Numerico: ',conteudo.isalnum())
print('-> Alfanumerico: ',conteudo.isalnum())
print('-> Ascii: ', conteudo.isascii())
print('-> Digit: ', conteudo.isdigit())
print('-> Lower: ', conteudo.islower())
print('-> Identifier: ', conteudo.isidentifier())


