"""Exercício criado por: https://www.cursoemvideo.com/
086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores
lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta."""


matrix = [0, 0, 0], \
         [0, 0, 0], \
         [0, 0, 0]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
print('-='*30)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f'[{matrix[i][j]:^5}]', end='')
    print()
