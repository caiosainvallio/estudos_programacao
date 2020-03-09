"""Exercício criado por : https://www.cursoemvideo.com/
025 Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome"""


nome = input('Digite seu nome completo: ')
if 'SILVA' in nome.upper():
    print('Você tem Silva no nome')
else:
    print('Você não tem Silva no nome')
