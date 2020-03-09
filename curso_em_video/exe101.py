"""Exercício criado por: https://www.cursoemvideo.com/
101: Crie um programa que tenha uma função chamada voto() que vai receber como
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando
se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""


def voto(ano):
    """
    Recebe o ano e informa a idade e se:
    idade < 18 = NÃO VOTA
    idade >= 18 and idade < 65 = VOTO OBRIGATÓRIO
    idade >= 65 VOTO OPCIONAL
    :param ano: ano de nascimento
    :return: idade e expressão
    """
    from datetime import date
    idade = date.today().year - ano
    if idade < 18:
        vota = 'NÃO VOTA'
    elif idade < 65:
        vota = 'VOTO OBRIGATÓRIO'
    else:
        vota = 'VOTO OPCOPNAL'
    return print(f'Com {idade} anos: {vota}.')


print('-'*30)
ano = int(input('Em que ano você nasceu? '))
voto(ano)
