"""Exercício criado por: https://www.cursoemvideo.com/
072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""


n = int(input('Digite um númenro entre 0 e 20: '))
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while n < 0 or n > 20:
    n = int(input('Tente novamente. Digite um númenro entre 0 e 20: '))
print(f'Você digitou o número {numeros[n]}')
