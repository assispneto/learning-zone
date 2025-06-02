#################### Interrupção usando WHILE: Break ####################

# Break         -> para um while há qualquer momento
# 'while True:' -> loop infinito
valor = soma = 0
while True:
    valor = int(input('Digite um número [999 para]> '))
    if (valor == 999):
        break
    soma = soma+valor
print('Print 1: Resultado da soma dos números digitados: {}'.format(soma))


 