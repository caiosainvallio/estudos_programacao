"""Exercício criado por : https://www.cursoemvideo.com/
039 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade:
* Se ele ainda vai se alistar ao serviço militar
* Se é a hora de se alistar
* Se já passou do tempo do alistamento"""

from datetime import date

ano = int(input('Informe o ano de nascimento: '))

idade = date.today().year - ano

if idade < 18:
    print('Faltam {} anos para você se alistar.'.format(18 - idade))
elif idade == 18:
    print('Você precisa se alistar esse ano.')
else:
    print('ATENÇÃO! Você oassou {} anos do periodo de alistamento, entre em contado.'.format(idade - 18))
