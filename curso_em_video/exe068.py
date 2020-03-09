"""Exercício criado por : https://www.cursoemvideo.com/
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo"""
from random import randint


print('=-'*15 + '\nVAMOS JOGAR PAR OU ÍMPAR\n' + '=-'*15)
cont = 0
while True:
    n_usu = int(input('Diga um valor: '))
    pi_usu = input('Par ou Ímpar? [P/I]: ').upper()
    print('--'*15)
    n_com = randint(1, 5)
    soma = n_usu + n_com
    result = 'Par' if soma % 2 == 0 else 'Ímpar'
    print(f'Você jogou {n_usu} e o computador {n_com}. Total de {soma} DEU {result.upper()}')
    print('--' * 15)
    if pi_usu == 'P' and result == 'Par' or pi_usu == 'I' and result == 'Ímpar':
        print('Você VENCEU!\nVamos jogar novamente...\n' + '=-'*15)
        cont += 1
    else:
        print('Você PERDEU!\n' + '=-'*15)
        break
print(f'GAME OVER! Você venceu {cont} vezes.')
