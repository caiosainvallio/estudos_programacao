"""Exercício criado por : https://www.cursoemvideo.com/
006 Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada"""


n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, n * 2))
print('O tríplo de {} vale {}.'.format(n, n * 3))
print('A raiz quadrada de {} é igulal a {:.2f}.'.format(n, n ** (1 / 2)))
