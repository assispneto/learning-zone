# Programa que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas as letras maiúsculas e minúsculas.
# -> Quantas letras ao todo (sem considerar espaços).
# -> Quantas letras tem o primeiro nome.

nome = str(input('Qual seu nome completo? ')).strip()
# o '.strip()' serve para eliminar os espaços antes e depois na frase

nomeMaiusculo   = nome.upper()
nomeMinusculo   = nome.lower()
fraseJunta      = nome.split()
primeiroNome    = fraseJunta[0]

tamanhoNome     = (len(nome) - nome.count(' '))
# o tamanho total do nome (len(nome)) menos o total de espaços que foram encontrados

tamPrimeiroNome = nome.find(' ')
# procura o primeiro espaço e retorna a contagem até lá


print(nomeMaiusculo)
print(nomeMinusculo)
print(primeiroNome)
print(tamanhoNome)
print(tamPrimeiroNome)


