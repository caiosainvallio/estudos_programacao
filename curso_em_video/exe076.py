"""Exercício criado por: https://www.cursoemvideo.com/
076: Crie um programa que tenha uma tupla única com nomes de produtos e seus
respectivos preços, na sequência. No final, mostre uma listagem de preços,
organizando os dados em forma tabular."""

prod = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2,
        'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-'*50)
for i in range(0, len(prod), 2):
    print('{:.<40}R$'.format(prod[i]), f'{prod[i + 1]:7.2f}')
print('-'*50)
