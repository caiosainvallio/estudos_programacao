"""Exercício criado por: https://www.cursoemvideo.com/
097: Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem
com tamanho adaptável."""


def titulo(texto):
    n = len(texto) + 10
    print('~'*n)
    print(' '*5 + texto.title() + ' '*5)
    print('~'*n)


titulo('início do programa')
titulo('fim do programa')
titulo('resultados')
