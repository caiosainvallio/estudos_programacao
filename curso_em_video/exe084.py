"""Exercício criado por: https://www.cursoemvideo.com/
084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""


temp = []
princ = []
maior = menor =0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    sn = str(input('Quer continuar? [s/n] '))
    if sn in 'n':
        break
print('-='*30)
print(princ)
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {maior}kg. Peso de', end=' ')
for i in princ:
    if i[1] == maior:
        print(i[0], end=' ')
print(f'\nO menor peso foi de {menor}kg. Peso de', end=' ')
for i in princ:
    if i[1] == menor:
        print(i[0], end=' ')
