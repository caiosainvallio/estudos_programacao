"""Exercício criado por : https://www.cursoemvideo.com/
017 Fça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hiotenusa."""


cat_op = float(input('Comprimento do cateto oposto: '))
cat_ad = float(input('Comprimento do cateto adjacente: '))
hip = (cat_op**2 + cat_ad**2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hip))
