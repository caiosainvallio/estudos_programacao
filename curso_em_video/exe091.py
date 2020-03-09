"""Exercício criado por: https://www.cursoemvideo.com/
091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número no dado."""
from random import randint
from time import sleep
from operator import itemgetter


jogadas = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
ranking = list()
print('Valores sorteados:')
for c, v in jogadas.items():
    print(f'O {c} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('-='*15)
print('\t= RANKING DOS JOGADORES =')
for i, v in enumerate(ranking):
    print(f'\t{i + 1}o lugar: {v[0]} com {v[1]}')
