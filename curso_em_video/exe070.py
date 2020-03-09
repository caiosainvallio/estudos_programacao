"""Exercício criado por : https://www.cursoemvideo.com/
070 Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final mostre:
a) Qual é o total gasto na compra
b) Quantos produtos custam mais de R$1000,00
c) Qual é o nome do produto mais barato."""
print('-'*50)
print('{:^50}'.format('LOJA SUPER BARATÃO'))
print('-'*50)
total = menor = mais_1k = c = 0
nome_menor = ''
while True:
    nome = input('Nome do produto: ').strip().title()
    preco = float(input('Preço R$'))
    c += 1
    total += preco
    if c == 1 or preco < menor:
        menor = preco
        nome_menor = nome
    if preco >= 1000:
        mais_1k += 1
    continuar = input('Quer continuar? [s/n] ').upper()
    while continuar not in 'SN':
        continuar = input('Quer continuar? [s/n] ').upper()
    if continuar == 'N':
        break
print('{:-^50}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais_1k} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {nome_menor} que custa R${menor:.2f}')
