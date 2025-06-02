# Crie um programa que faça o computador jogar Jokenpô com você.


from random import randint

print('1 - PEDRA')
print('2 - PAPEL')
print('3 - TESOURA')
escolhaUser = int(input('Qual sua escolha? '))

escolhaComput = randint(1, 3)

# Usuario escolhe pedra
if escolhaUser==1 and escolhaComput==1:
    print('Empate')
elif escolhaUser==1 and escolhaComput==2:
    print('O computador escolheu papel, você perdeu!')
elif escolhaUser==1 and escolhaComput==3:
    print('O computador escolheu tesoura, você ganhou!')
# Usuario escolhe papel
elif escolhaUser==2 and escolhaComput==1:
    print('O computador escolheu pedra, você ganhou!')
elif escolhaUser==2 and escolhaComput==2:
    print('Empate')
elif escolhaUser==2 and escolhaComput==3:
    print('O computador escolheu tesoura, você perdeu!')
# Usuario escolhe tesoura
elif escolhaUser==3 and escolhaComput==1:
    print('O computador escolheu pedra, você perdeu!')
elif escolhaUser==3 and escolhaComput==2:
    print('O computador escolheu papel, você ganhou!')
elif escolhaUser==3 and escolhaComput==3:
    print('Empate')


