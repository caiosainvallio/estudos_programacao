"""Exercício criado por: https://www.cursoemvideo.com/
099: Faça um programa que tenha uma função chamada maior(), que receba
vários parâmetros com valores inteiros. Seu programa tem que analisar
todos os valores e dizer qual deles é o maior."""
from time import sleep


def valores(*val):
    print('-='*30)
    print('Analizando os valores passados...')
    sleep(0.4)
    maior = cont = 0
    for i in val:
        print(i, end=' ')
        if i > maior:
            maior = i
        cont += 1
        sleep(0.3)
    print(f'Foram analizados {cont} valores ao todo.')
    print(f'O maior valor informado foi p {maior}.')


valores(2, 9, 4, 5, 7, 1)
valores(4, 7, 0)
valores(1, 2)
valores(6)
valores()
