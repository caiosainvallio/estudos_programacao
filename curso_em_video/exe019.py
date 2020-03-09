"""Exercício criado por : https://www.cursoemvideo.com/
019 Um professor quer sortear um dos seus quatro alunos para apagra o quadro.
Faça um programa que ajude ele,  lendo o nome deles escrevendo o nome do escolhido."""
import random


a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
escolha = random.choice([a1, a2, a3, a4])
print('O aluno escolhido foi {}'.format(escolha))
