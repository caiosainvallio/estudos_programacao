"""Exercício criado por : https://www.cursoemvideo.com/
027 Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente."""


nome = input('Digite seu nome completo: ').strip()
print('Primeiro nome: {}'.format(nome.title().split()[0]))
print('Último nome: {}'.format(nome.title().split()[-1]))
