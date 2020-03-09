"""Exercício criado por: https://www.cursoemvideo.com/
071 Crie um programa que simule o funcionamenrto de um caixa eletrônico. No início, pergunte
ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.
OBS. Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""


print('='*40)
print('{:^40}'.format('BANCO CEV'))
print('='*40)
valor = int(input('Qual valor você quer sacar? R$'))
notas = [50, 20, 10, 1]
for nota in notas:
    ced = valor // nota
    if ced > 0:
        print(f'Total de {ced} cédulas de R${nota}')
    valor = valor - ced * nota
print('='*40 + '\nVolte sempre ao BANCO CEV! Tenha um bom dia!')
