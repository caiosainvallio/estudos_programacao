"""Exercício criado por : https://www.cursoemvideo.com/
052 Faça um programa que leia um número inteiro e diga se ele é ou não um número primo"""


n = int(input('Digite o número para saber se primo: '))
soma = 0
for i in range(1, n + 1):
    if n % i == 0:
        soma += 1
if soma == 2:
    print('É primo.')
else:
    print('Não é primo.')
