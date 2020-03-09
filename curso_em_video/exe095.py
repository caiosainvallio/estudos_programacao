"""Exercício criado por: https://www.cursoemvideo.com/
095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador."""


camp = dict()
lista = []
while True:
    camp['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {camp["nome"]} jogou? '))
    gols = []
    soma = 0
    for p in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {p + 1}? ')))
        soma += gols[p]
    camp['gols'] = gols[:]
    camp['total'] = soma
    lista.append(camp.copy())
    camp.clear()
    sn = str(input('Quer continuar? [s/n] '))
    if sn in 'n':
        break

print('-='*25)
print('cod ', end='')
for i in lista[0].keys():
    print(f'{i:<15}', end='')
print()
print('-'*50)
for k, v in enumerate(lista):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*50)
while True:
    n = int(input('Mostrar dados de qual jogador? '))
    while n > len(lista):
        print(f'ERRO! Não exite jogador com código {n}!\nTente novamente ou 99 para sair')
        n = int(input('Mostrar dados de qual jogador? '))
        if n == 99:
            break
    if n == 99:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {lista[n]["nome"]}:')
    for n, i in enumerate(lista[n]["gols"]):
        print(f'\tNo jogo {n}, fez {i} gols.')
    print('-'*50)
