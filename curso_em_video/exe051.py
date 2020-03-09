"""Exercício criado por : https://www.cursoemvideo.com/
051 Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No no final, mostre os 10 primeiros termos dessa progressão"""


termo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
print(termo, end=' ')
for i in range(1, 10):
    termo += razao
    print(termo, end=' ')
