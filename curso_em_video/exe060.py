"""Exercício criado por : https://www.cursoemvideo.com/
060 Faça um programa que leia um número qualquer e mostre o seu fatorial."""


n = int(input('Digite um valor: '))
i = 0
fat = 1
while i < n:
    i += 1
    fat *= i
print('{}! = {}'.format(n, fat))
