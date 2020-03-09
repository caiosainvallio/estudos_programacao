"""Exercício criado por : https://www.cursoemvideo.com/
041 A Confederação Nacional de Natação precisa se um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
* Até 9 anos: MIRIM
* Até 14 anos: INFANTIL
* Até 19 anos: JUNIOR
* Até 20 anos:SÊNIOR
* Acima: MASTER"""
from datetime import date


ano = int(input('Informe o ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Idade: {}\nStatus: MIRIM.'.format(idade))
elif idade <= 14:
    print('Idade: {}\nStatus: INFANTIL'.format(idade))
elif idade <= 19:
    print('Idade: {}\nStatus: JUNIOR'.format(idade))
elif idade <=20:
    print('Idade: {}\nStautus: SÊNIOR'.format(idade))
else:
    print('Idade: {}\nStatus: MASTER'.format(idade))
