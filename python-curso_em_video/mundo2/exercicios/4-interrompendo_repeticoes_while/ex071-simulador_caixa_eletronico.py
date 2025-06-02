# Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues. 
# -> OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


################### Resolução Prof. G. Guanabara ###################

print('\n|----------------------------------|')
print('|           BANCO DO CEV           |')
print('|----------------------------------|')

valor       = int(input('# Qual o valor de saque? > R$'))
total       = valor
ced         = 50
totalCedula = 0

while True:
    if (total>=ced):
        total       = total-ced
        totalCedula = totalCedula+1
    else:
        if (totalCedula>0):
            print(f'# {totalCedula} cedulas de R${ced}\n')
        if (ced == 50):
            ced = 20
        elif (ced == 20):
            ced = 10
        elif (ced == 10):
            ced = 1
        totalCedula = 0
        if (total == 0):
            break


