"""Exercício criado por : https://www.cursoemvideo.com/
023 Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados"""


n = input('Digite um número entre 0 e 9999: ')
print('unidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}'.format(n[3], n[2], n[1], n[0]))
