"""Exercício criado por: https://www.cursoemvideo.com/
075: Desenvolva um programa que leia quatro valores pelo teclado e
guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""


num = [int(input('Digite um número: '))]
for i in range(3):
    num.append(int(input('Digite outro número: ')))
num = tuple(num)
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}a posição')
else:
    print('O valor 3 não apareceu')
print('os valores pares digitados foram ', end='')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')
