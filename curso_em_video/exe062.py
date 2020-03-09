"""Exercício criado por : https://www.cursoemvideo.com/
062 Ler o primeiro termo e a razão de uma PA, mostre os
10 primeiros termos da progressão usando a estrutura while.
Perguntar para o usuário se ele quer mostrar mais termos,
e quantos ele quer. O programa encerra qundo o usuário
disser que quer visualizar mais 0 termos"""


termo = int(input('Digitar o primero termo da PA: '))
razao = int(input('Digitar razao da PA: '))
c = 0
pa = []
while c < 10:
    pa.append(termo)
    termo += razao
    c += 1
print(pa)
n = 1
while n != 0:
    n = int(input('Você gostaria de visualisar mais quantos termos? '))
    pa = [pa[-1]]
    c = 0
    if n != 0:
        while c < n:
            pa.append(termo)
            termo += razao
            c += 1
        print(pa)
    else:
        break
print('Fim do programa')
