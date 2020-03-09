"""Exercício criado por : https://www.cursoemvideo.com/
054 Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas aisnda não atingiram a maioridade e quantos já são maiores"""
from datetime import date


maior = 0
menor = 0
for i in range(7):
    ano = int(input('Ano da {}a pessoa: '.format(i + 1)))
    if abs(date.today().year - ano) >= 18:
        maior += 1
    else:
        menor += 1
print('{} menores\n{} maiores'.format(menor, maior))
