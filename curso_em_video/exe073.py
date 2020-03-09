"""Exercício criado por: https://www.cursoemvideo.com/
073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""


times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico - PR', 'São Paulo',
         'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco',
         'Atlético - MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA',
         'Chapecoense', 'Avaí')
chap = times.index('Chapecoense')
print('-='*40)
print(f'Lista de times do brasileirão: {times}')
print('-='*40)
print(f'Os 5 primeiros são: {times[:5]}')
print('-='*40)
print(f'os 4 últimos são: {times[-4:]}')
print('-='*40)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*40)
print(f'O Chapecoense está na {chap}a posição')
