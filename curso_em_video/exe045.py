"""Exercício criado por : https://www.cursoemvideo.com/
045 Crie um programaque faça o computador jogar JOKENPÔ com você."""
from random import randint
from time import sleep


print('Vamos jogar jokenpô?')
dicionario = {1: 'PEDRA', 2: 'PAPEL', 3: 'TESOURA'}
ponto_u = 0
ponto_c = 0
rodada = 1
while ponto_u < 3 and ponto_c < 3:
    c = randint(1, 3)
    u = int(input('''
    #######################
    Rodada {}:
    
    Pontuação:
    você {} x {} computador
    
    Selecione uma opção:

    Para PEDRA   digite 1
    Para PAPEL   digite 2
    Para TESOURA digite 3
    '''.format(rodada, ponto_u, ponto_c)))
    print('\tJO')
    sleep(0.5)
    print('\tKEN')
    sleep(0.5)
    print('\tPO!!!')
    sleep(0.5)
    if u == 1 and c == 2 or u == 2 and c == 3 or u == 3 and c == 1:
        print('\t{} ganha de {}!'.format(dicionario[u], dicionario[c]))
        ponto_u += 1
    elif u == 1 and c == 3 or u == 2 and c == 1 or u == 3 and c == 2:
        print('\t{} perde de {}...'.format(dicionario[u], dicionario[c]))
        ponto_c += 1
    else:
        print('\t{} empada com {}'.format(dicionario[u], dicionario[c]))
    rodada += 1
if ponto_u == 3:
    print('='*25 + '\nPARABÉNS!!! Você ganhou!\n' + '='*25)
else:
    print('='*20 + '\nVocê perdeu...\n' + '='*20)
