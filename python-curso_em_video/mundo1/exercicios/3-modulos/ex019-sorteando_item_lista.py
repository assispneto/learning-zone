# Ler nome dos alunos e escrevendo na tela o nome do escolhido

import random

v1 = input('Aluno 1: ')
v2 = input('Aluno 2: ')
v3 = input('Aluno 3: ')
v4 = input('Aluno 4: ')

lista = [v1, v2, v3, v4]

sorteio = random.choice(lista)  #Escolhe um numero dentro dos listados
print(sorteio)



