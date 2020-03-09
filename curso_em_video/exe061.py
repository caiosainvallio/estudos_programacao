"""Exercício criado por : https://www.cursoemvideo.com/
061 Ler o primeiro termo e a razão de uma PA, mostre os
10 primeiros termos da progressão usando a estrutura while."""


termo = int(input('Digitar o primero termo da PA: '))
razao = int(input('Digitar razao da PA: '))
c = 0
pa = []
while c < 10:
    pa.append(termo)
    termo += razao
    c += 1
print(pa)
