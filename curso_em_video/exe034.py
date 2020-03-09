"""Exercício criado por : https://www.cursoemvideo.com/
034 Escreva um programa que pergunte o salário e calcule o valor do seu aumento.

Para salários superiores a R$1250,00, calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%."""

sal = float(input('Qual o salário do funcionáio: '))
aumento = sal * 0.1 if sal > 1250 else sal * 0.15
'''
if sal > 1250:
    aumento = sal * 0.1
else:
    aumento = sal * 0.15
'''
print('O salario com ajustado é de R${:.2f}'.format(sal + aumento))
