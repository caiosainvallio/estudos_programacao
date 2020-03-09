"""Exercício criado por : https://www.cursoemvideo.com/
004 Faça um programa que leia algo pelo teclado e mostre na tela o seu
tipo primitivo e todas as informações possíveis sobre ele."""


algo = input('Digite algo: ')
print('O tipo primitivo deste valor é {}'.format(type(algo)))
print('Só tem espaços? {}'.format(algo.isspace()))
print('É um número? {}'.format(algo.isnumeric()))
print('É alfanumérioca? {}'.format(algo.isalnum()))
print('É alfabético? {}'.format(algo.isalpha()))
print('Está em maiúsculas? {}'.format(algo.isupper()))
print('Está em minúsculas? {}'.format(algo.islower()))
print('Está captalizada? {}'.format(algo.istitle()))
