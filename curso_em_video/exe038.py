"""Exercício criado por : https://www.cursoemvideo.com/
038 Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela um mensagem:
* O primeiro valor é maior
* O segundo valor é maior
* Não existe valor maior, os dois são iguais"""

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))

if a > b:
    print('O primeiro número é maior.')
elif a < b:
    print('O segundo número é maior.')
else:
    print('Os números são iguais.')
