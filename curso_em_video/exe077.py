"""Exercício criado por: https://www.cursoemvideo.com/
 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
 Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""


pal = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
       'esstudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for i in pal:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for j in i.lower():
        if j in 'aeiou':
            print(j, end=' ')
