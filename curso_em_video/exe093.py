"""Exercício criado por: https://www.cursoemvideo.com/
093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai
ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado
em um dicionário, incluindo o total de gols feitos durante o campeonato."""


camp = dict()
camp['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {camp["nome"]} jogou? '))
gols = []
soma = 0
for p in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {p + 1}? ')))
    soma += gols[p]
camp['gols'] = gols[:]
camp['total'] = soma
print('-='*30)
print(camp)
print('-='*30)
for c, v in camp.items():
    print(f'O campo {c} tem o valor {v}.')
print('-='*30)
print(f'O jogador {camp["nome"]} jogou {partidas} partidas.')
for p in range(partidas):
    print(f'\t=> Na partida {p + 1}, fez {camp["gols"][p]} gols.')
print(f'Foi um total de {camp["total"]} gols.')
