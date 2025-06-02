# Programa que ler uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez

frase       = str(input('Digite uma frase: ')).strip()

fraseLower  = frase.lower()
letraA      = fraseLower.count('a')
posicaoA    = fraseLower.find('a')+1
ultimoA     = fraseLower.rfind('a')+1  # Começa procurar da direita para esquerda

print('Nessa frase, a letra "A" é mostrada {} vezes'.format(letraA))
print('A primeira vez que "A" aparece é na posição: {}'.format(posicaoA))
print('A última vez que "A" aparece é na posição: {}'.format(ultimoA))


