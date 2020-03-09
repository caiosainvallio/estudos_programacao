"""Exercício criado por : https://www.cursoemvideo.com/
057 Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
M ou F. Caso esteja errado, peça a digitação novamente até ter um valor correto"""


sexo = ''
while sexo != 'm' and sexo != 'f':
    sexo = input('Qual  o seu sexo? [m/f] ')
