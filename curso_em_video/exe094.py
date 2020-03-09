"""Exercício criado por: https://www.cursoemvideo.com/
094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""


lista = []
pessoas = {}
soma = cont = 0
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    sexo = str(input('Sexo: [f/m] '))
    idade = int(input('Idade: '))
    pessoas = {'nome': nome, 'sexo': sexo, 'idade': idade}
    lista.append(pessoas)
    soma += idade
    cont += 1
    sn = str(input('Quer continuar? [s/n] '))
    if sn in 'n':
        break
print('-='*30)
print(f'O grupo tem {len(lista)} pessoas.')
print(f'A média de idade é {soma/len(lista):.2f} anos.')
print('As mulhres cadastradas foram:', end=' ')
for pessoa in lista:
    if pessoa['sexo'] == 'f':
        print(f'{pessoa["nome"]}', end=' ')
print('\nLista das pessoas que estão acima da média:')
for pessoa in lista:
    if pessoa['idade'] > soma/len(lista):
        print(f'Nome = {pessoa["nome"]}; sexo = {pessoa["sexo"]}; idade = {pessoa["idade"]};')
        print()
print('<< ENCERRADO >>')
