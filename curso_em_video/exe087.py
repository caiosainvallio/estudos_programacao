"""Exercício criado por: https://www.cursoemvideo.com/
087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""


matrix = [0, 0, 0], \
         [0, 0, 0], \
         [0, 0, 0]
par = t_col = 0
lin = list()
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
print('-='*30)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f'[{matrix[i][j]:^5}]', end='')
    print()
print('-='*30)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] % 2 == 0:
            par += matrix[i][j]
        if j == 2:
            t_col += matrix[i][j]
        if i == 1:
            lin.append(matrix[i][j])
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {t_col}')
print(f'O maior valor da segunda linha é {max(lin)}')
