"""Exercício criado por: https://www.cursoemvideo.com/
078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
posições na lista."""


val = []
maior = menor = 0
for i in range(5):
    n = int(input(f'Digite um valor para a posição {i}: '))
    val.append(n)
print('=-'*30)
print(f'Você digitou os valores {val}')
print(f'O maior valor digitado foi {max(val)} nas posições', end=' ')
for i, n in enumerate(val):
    if n == max(val):
        print(f'{i}...', end=' ')
print(f'\nO menor valor digitado foi {min(val)} nas posições', end=' ')
for i, n in enumerate(val):
    if n == min(val):
        print(f'{i}...', end=' ')
