"""Exercício criado por : https://www.cursoemvideo.com/
035 Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo"""

l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 > abs(l2 - l3) and l2 > abs(l1 - l3) and l3 > abs(l1 - l2):
        print('Estes valores fomam um triângulo!')
    else:
        print('Esses valores não fomam um triângulo...')
else:
    print('Esses valores não fomam um triângulo...')
