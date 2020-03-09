"""Exercício criado por: https://www.cursoemvideo.com/
074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
valor que estão na tupla."""
from random import randint


num = []
for i in range(5):
    num.append(randint(1, 9))
num = tuple(num)
maior = menor = 0
print('Os valores sorteados foram:', end=' ')
for i, n in enumerate(num):
    if i == 0 or n < menor:
        menor = n
    if n > maior:
        maior = n
    if i < 4:
        print(n, end=' ')
    else:
        print(n)
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
