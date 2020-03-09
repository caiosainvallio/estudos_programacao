"""Exercício criado por: https://www.cursoemvideo.com/
081: Crie um programa que vai ler vários números e colocar
em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""


lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    sn = input('Quer continuar? [s/n] ')
    cont += 1
    while not sn in 'sn':
        sn = input('Quer continuar? [s/n] ')
    if sn == 'n':
        break
print('-=' * 30)
print(f'Você digitou {cont} elementos')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não faz parte da lista!')
