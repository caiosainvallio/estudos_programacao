"""Exercício criado por: https://www.cursoemvideo.com/
092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente
de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""
from datetime import datetime


cadastro = {}
while True:
    cadastro['nome'] = str(input('Nome: '))
    cadastro['idade'] = datetime.today().year - int(input("Ano de nascimento: "))
    cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
    if cadastro['ctps'] == 0:
        print('-=' * 20)
        for c, v in cadastro.items():
            print(f'{c} tem o valor de {v}')
        break
    else:
        cadastro['contratação'] = int(input('Ano de contratação: '))
        cadastro['salário'] = float(input('Salário: R$'))
        cadastro['aposentadoria'] = cadastro['idade'] - (datetime.today().year - cadastro['contratação']) + 35
        print('-=' * 20)
        for c, v in cadastro.items():
            print(f'{c} tem o valor de {v}')
        break
