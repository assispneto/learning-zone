# Escreva um programa que leia um número N inteiro qualquer e 
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

print('\n>----------- Sequência de Fibonacci -----------<')

n       = int(input('Quantos termos da sequência devem ser mostrados > '))
cont    = 0
fib     = 0
termo1  = 0
termo2  = 1

print('{} -> {}'.format(termo1, termo2), end='')
cont = (cont+3)       # Faço isso pq vou iniciar já mostrando os dois primeiros

while cont<=n:
    fib     = (termo1+termo2)               # Somos os dois *últimos* termos
    print(' -> {}'.format(fib), end='')
    termo1  = termo2                        # O primeiro termo passa a ser o segundo
    termo2  = fib                           # O segundo termo vai ser o valor encontrado na soma dos 2 primeiros
    cont    = (cont+1)
print(' -> FIM')
    

    