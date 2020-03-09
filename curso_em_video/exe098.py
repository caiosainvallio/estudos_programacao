"""Exercício criado por: https://www.cursoemvideo.com/
098: Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa
tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""
from time import sleep


def contagem(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    for n in range(inicio, fim, passo):
        print(n, end=' ')
        sleep(0.5)
    print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, -2)

print('Agora é sua vez de realizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
