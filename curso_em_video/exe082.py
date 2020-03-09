"""Exercício criado por: https://www.cursoemvideo.com/
082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores
pares e os valores ímpares digitados, respectivamente. Ao final, mostre o
conteúdo das três listas geradas."""


lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    elif n % 2 != 0:
        impar.append(n)
    sn = input('Quer continuar? [s/n] ')
    while not sn in 'sn':
        sn = input('Quer continuar? [s/n] ')
    if sn in 'n':
        break
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
