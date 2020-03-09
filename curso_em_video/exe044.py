"""Exercício criado por : https://www.cursoemvideo.com/
044 Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
* À vista dinheiro/cheque: 10% de desconto
* À vista no carão: 5% de desconto
* Em ate 2x no cartão: preço normal
* 3x ou mais no cartão: 20% de juros"""


valor = float(input('Digite o valor do produto: '))
forma = int(input('''
Informe a forma de pagamento:

Dinheiro/cheque (10% de desconto):   Digite 1
À vista no cartão (5% de desconto):  Digite 2
2x no cartão (sem desconto):         Digite 3
3x ou mais no cartao (20% de juros): Digite 4

'''))
dicionario = {1: 'Dineiro/cheque',
              2: 'À vista no cartão',
              3: '2x no cartão',
              4: '3x ou mais no cartão'}
if forma == 1:
    total = valor - valor * 0.1
elif forma == 2:
    total = valor - valor * 0.05
elif forma == 3:
    total = valor
else:
    total = valor + valor * 0.2
print('''
Obrigado por realizar sua compra conosco!

Forma de pagamento escolhida: {}
Valor total: R${:.2f}
'''.format(dicionario[forma], total))
