"""Exercício criado por: https://www.cursoemvideo.com/
096: Faça um programa que tenha uma função chamada área(), que receba as
dimensões de um terreno retangular (largura e comprimento) e mostre a área
do terreno."""


def area(largura, comprimento):
    print(f'A área de um terreno de {largura:.1f}x{comprimento:.1f} é de {largura*comprimento:.1f}m2.')


print('Controle de terrenos')
print('-'*20)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
