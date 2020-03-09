"""Exercício criado por : https://www.cursoemvideo.com/
013 Faça um algoritmo que leia o salário e mostre seu novo salário, com 15% de aumento."""


n = float(input('Qual é o salário do Funcionário? R$'))
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(n, n+n*0.15))
