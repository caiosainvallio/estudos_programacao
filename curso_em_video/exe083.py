"""Exercício criado por: https://www.cursoemvideo.com/
083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e
fechados na ordem correta."""


exp = input('Digite a expressão: ')
cont_a = cont_f = 0
for i in exp:
    if i == '(':
        cont_a += 1
    if i == ')':
        cont_f += 1
if cont_a == cont_f:
    print('A expresssão está correta!')
else:
    print('A expressão está errada!')
