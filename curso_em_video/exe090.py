"""Exercício criado por: https://www.cursoemvideo.com/
090: Faça um programa que leia nome e média de um aluno, guardando também
 a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela."""


nome = str(input('Nome: ')).strip().capitalize()
media = float(input(f'Média de {nome}: '))
boletim = {'Nome': nome, 'Média': media}
if boletim['Média'] >= 7:
    boletim['Situação'] = 'Aprovado'
else:
    boletim['Situação'] = 'Reprovado'
for c, v in boletim.items():
    print(f'{c} é igual a {v}')
