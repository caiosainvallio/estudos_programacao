"""Exercício criado por : https://www.cursoemvideo.com/
053 Crie um programa que leia uma frase qualquer e diga
se ela é um palíndromo, desconsiderando os espaços"""


frase = input('Digite uma frase: ').strip().lower()
frase = frase.split()
frase = ''.join(frase)
if frase == frase[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')
