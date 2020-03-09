"""Exercício criado por : https://www.cursoemvideo.com/
009 Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada."""


n = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
for i in range(1, 11):
    print('{} x {} = {}'.format(n, i, i*n))
print('-'*12)
