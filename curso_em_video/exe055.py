"""Exercício criado por : https://www.cursoemvideo.com/
055 Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e menor peso lidos"""


menor = 999
maior = 10
for i in range(5):
    peso = int(input('Peso da {}a pessoa: '.format(i + 1)))
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso
print('Maior peso {}\nMenor peso {}'.format(maior, menor))
