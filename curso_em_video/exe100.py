"""Exercício criado por: https://www.cursoemvideo.com/
100: Faça um programa que tenha uma lista chamada números e duas
funções chamadas sorteia() e somaPar(). A primeira função vai sortear
5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores pares sorteados pela função anterior."""
from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando 5 valores da lista:', end=' ')
    for i in range(5):
        n = randint(1, 9)
        print(n, end=' ')
        lista.append(n)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    sleep(0.3)
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
