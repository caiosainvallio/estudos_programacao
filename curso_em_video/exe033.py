"""Exercício criado por : https://www.cursoemvideo.com/
033 Façå um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR."""

n1 = float(input('Primero número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))

maior = 0

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

print('O numero maior é {}'.format(maior))

menor = 0

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3

print('O número menor é {}'.format(menor))
