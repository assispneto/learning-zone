# Ler o nome de 4 alunos e mostra a ordem sorteada

import random

v1 = str(input('Aluno 1: '))
v2 = str(input('Aluno 2: '))
v3 = str(input('Aluno 3: '))
v4 = str(input('Aluno 4: '))

lista = [v1, v2, v3, v4]

random.shuffle(lista)   # Embaralha a lista

print('A ordem do sorteio é: {}'.format(lista))


