"""Exercício criado por : https://www.cursoemvideo.com/
028 Escreva um programa que faça o computador 'pensar' em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
número escolhido pelo computador.

O programa deverá escrever na tela se o usu;ario venceu ou perdeu."""
import random
from time import sleep


print('Olá usuário, vamos joagr um jogo?\n\nEu vou pensar em um número e você irá tentar acertar!')
n = int(input('\n Digite um número entre 0 e 5: '))
comp = random.randint(0, 5)
print('Processando...')
sleep(2)
if n == comp:
    print('Parabéns!!! Você acertou!!!')
else:
    print('A ha! Você errou! Eu pensei em {} e você falou {}!'.format(comp, n))
