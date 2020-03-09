"""Exercício criado por : https://www.cursoemvideo.com/
036 Escreva um programa para aprovar o emprástimo bancário para a compra de uma casa.
O Programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado."""

casa = float(input('Valor da casa: '))
sal = float(input('Salário: '))
anos = int(input('Anos: '))

mes = anos * 12

prestacao = casa / mes

if prestacao > sal + sal * 0.3:
    print('Impréstimo negado. O valor da prestação R${:.2f} excede em 30% o valor do salário R${:.2f}'. format(prestacao, sal))
else:
    print('Impréstimo concedido!\nValor da prestação: R${:.2f}\nNúmero de prestaçoes: {}'.format(prestacao, mes))