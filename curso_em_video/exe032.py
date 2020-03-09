"""Exercício criado por : https://www.cursoemvideo.com/
032 Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO."""

from datetime import date
ano = int(input('Digite o ano que deseja saber (ou 0 para usar o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é bissexto!'.format(ano))
else:
    print('{} não é bissexto!'.format(ano))
