"""Exercício criado por : https://www.cursoemvideo.com/
050 Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor for ímpar, desconsicere-o"""


soma = 0
for i in range(0, 6):
    n = int(input('Digite o {}o valor: '.format(i + 1)))
    if n % 2 == 0:
        soma += n
print('Total: {}'.format(soma))
