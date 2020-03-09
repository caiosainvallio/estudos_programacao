"""Exercício criado por : https://www.cursoemvideo.com/
026 Faça um programa que leia uma frase pelo teclado e mostre:
* Quantas vezes aparece a letra A
* Em que posição ela aparece a primeira vez
* Em que posição ela parece a última vez"""


frase = input('Digite uma frase: ').strip()
print('Aletra a aparece {} vezes.'.format(frase.lower().count('a')))
print('A primeira vez que a letra a aparece é na {}a posição.'.format(frase.find('a')))
print('A última vez que a letra a aparece é na {}a posição.'.format(frase.rfind('a')))
