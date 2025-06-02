# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

escolha         = ''    # Par ou impar
valorEscolhido  = 0     # Numero do usuario
valorAleatorio  = 0     # Numero aleatorio do computador
consulta        = 0     # Variavel aux para consultar quem ganhou 
vitorias        = 0     # Para contar as vitorias do jogador

print('\n>-------PAR ou IMPAR-------<\n')
while True:
    # Recebo os valores
    escolha         = str(input('# PAR OU IMPAR > ')).lower()
    valorEscolhido  = int(input('#        VALOR > '))
    valorAleatorio  = random.randint(1, 10)
    # Realizo a soma dos valores para depois testar o 'par' ou 'impar'
    consulta        = (valorEscolhido+valorAleatorio)   
    # Verifico se o usuario realmente digitou PAR ou IMPAR
    while (escolha not in 'par') or (escolha not in 'impar'):
        print('####### ERROR #######')
        print('[Digite PAR ou IMPAR]')
        escolha         = str(input('# PAR OU IMPAR > ')).lower()
        valorEscolhido  = int(input('#        VALOR > '))
        consulta        = (valorEscolhido+valorAleatorio) 
        # ESCOLHEU PAR e o resultado realmente era par
    if (escolha in 'par') and (consulta%2 == 0):
        print(f'>--EU ESCOLHI {valorAleatorio}--<')
        print('>--VOCÊ VENCEU. VAMOS JOGAR MAIS UMA VEZ...\n')
        vitorias = vitorias+1
    # ESCOLHEU PAR e o resultado era impar
    elif (escolha in 'par') and (consulta%2 != 0):
        print(f'\n>--EU ESCOLHI {valorAleatorio}--<')
        print('>--VOCÊ PERDEU, BABACA!--<')
        break
    # ESCOLHEU IMPAR e o resultado realmente era impar
    elif (escolha in 'impar') and (consulta%2 != 0):
        print(f'>--EU ESCOLHI {valorAleatorio}--<')
        print('>--VOCÊ VENCEU. VAMOS JOGAR MAIS UMA VEZ...\n')
        vitorias = vitorias+1
    # ESCOLHEU IMPAR e o resultado  era par
    elif (escolha in 'impar') and (consulta%2 == 0):
        print(f'\n---> EU ESCOLHI {valorAleatorio}')
        print('---> VOCÊ PERDEU, BABACA!')
        break
# Depois de perder, o programa contabiliza as rodadas e faz uma pequena provocação para o user
if vitorias == 0:
    print('E não me venceu nehuma vez :P')
else:
    print(f'Mas ainda me venceu {vitorias} vezes!')


