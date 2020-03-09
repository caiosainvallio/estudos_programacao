"""Exercício criado por : https://www.cursoemvideo.com/
067 Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O prgrama será interrompido quando
o número solicitado for negativo"""


while True:
    n = int(input('Quer ver a tubauda de qual valor? '))
    if n <= 0:
        break
    print('-' * 30)
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
    print('-' * 30)
