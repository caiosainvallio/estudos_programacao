"""Exercício criado por : https://www.cursoemvideo.com/
022 Crie um programa que leia o nome completo de uma pessoa e mostre:

* O nome com todas as letras maiúsculas
* O nome com todas minísculas
* Quantas letras ao todo (sem considerar espaços).
* Quantas letras tem o primeiro nome."""


nome = input('Digite seu no e completo: ').strip()
print('Nome em maiúsculas: {}'.format(nome.upper()))
print('Nome em minúsculas: {}'.format(nome.lower()))
lista = nome.split()
total = 0
for i in range(0, len(lista)):
    total += len(lista[i])
print('Número de letras no total: {}'.format(total))
print('Número de letras do primeiro nome: {}'.format(len(lista[0])))
