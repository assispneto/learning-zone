# Refaça o DESAFIO 9, mostrando a tabuada de um número que 
# o usuário escolher, só que agora utilizando um laço for

valor = int(input('Qual o valor você deseja saber a tabuada? '))
for c in range(0, 11):
    print('{} x {:2} = {}'.format(valor, c, valor*c))


