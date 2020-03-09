"""Exercício criado por : https://www.cursoemvideo.com/
007 Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média."""


a1 = float(input('Primeira nota do aluno: '))
a2 = float(input('Segunda nota do aluno: '))
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(a1, a2, (a1+a2)/2))
