# Programa que ler o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

frase       = str(input('Digite seu nome completo: ')).strip()
fraseDiv    = frase.split()

primeiroNome    = fraseDiv[0]
ultimoNome      = fraseDiv[-1]

print('Seu primeiro nome: {}'.format(primeiroNome))
print('Seu último nome: {}'.format(ultimoNome))


