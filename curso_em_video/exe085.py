"""Exercício criado por: https://www.cursoemvideo.com/
085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre
os valores pares e ímpares em ordem crescente."""


lista = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o {i}o valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('-='*30)
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram: {sorted(lista[1])}')
