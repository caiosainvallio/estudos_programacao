"""Exercício criado por : https://www.cursoemvideo.com/
012 Faça um algoritmo que leia o preço de um produto e
mostre o seu novo preço, com 5% de desconto."""


n = float(input('Qual é o preço do produto? R$'))
print('O produto que custava R${:.2f}, na promoção com desonto de 5% vai custar R${:.2f}'.format(n, n-n*0.05))
