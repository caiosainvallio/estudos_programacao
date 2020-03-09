"""Exercício criado por : https://www.cursoemvideo.com/
049 Refaça o exe009, mostrando a tabuada de um número que o usuário
escolher, só que agora utilizando um laço for"""


n = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
for i in range(1, 11):
    print('{} x {} = {}'.format(n, i, i*n))
print('-'*12)
