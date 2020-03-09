"""Exercício criado por: https://www.cursoemvideo.com/
088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""
from random import randint
from time import sleep


print('-'*40)
print(f'{"JOGO DA MEGA SENA":^40}')
print('-'*40)
n = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = list()
jogo = list()
cont = 1
for i in range(1, n + 1):
    for j in range(6):
        jogo.append(randint(1, 60))
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    cont += 1
print('-='*5 + f' SORTEANDO {n} JOGOS ' + '-='*5)
sleep(1)
for i, j in enumerate(jogos):
    print(f'Jogo {i + 1}: {j}')
    sleep(1)
print('-='*6 + ' < BOA SORTE > ' + '-='*6)
