"""Exercício criado por: https://www.cursoemvideo.com/
089: Crie um programa que leia nome e duas notas de vários alunos e guarde
tudo em uma lista composta. No final, mostre um boletim contendo a média de
cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""


aluno = list()
boletim = list()
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    aluno.append(nome)
    nota_1 = float(input('Nota 1: '))
    aluno.append(nota_1)
    nota_2 = float(input('Nota 2: '))
    aluno.append(nota_2)
    media = (nota_1 + nota_2) / 2
    aluno.append(media)
    boletim.append(aluno[:])
    aluno.clear()
    sn = str(input('Quer continuar? [s/n] '))
    if sn in 'n':
        break
print('-='*20)
print(f'{"No.":<4}  {"NOME":<10}  {"MÉDIA":>10}')
print('--'*20)
for i, aluno in enumerate(boletim):
    print(f'{i:<4}  {aluno[0]:<10}  {aluno[3]:>10.1f}')
print('--'*20)
while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if mostrar == 999:
        break
    print(f'Notas de {boletim[mostrar][0]} são {boletim[mostrar][1:3]}')
