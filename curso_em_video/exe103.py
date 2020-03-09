"""Exercício criado por: https://www.cursoemvideo.com/
103: Faça um programa que tenha uma função chamada ficha(), que receba dois
parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
algum dado não tenha sido informado corretamente."""


def ficha(jog='<desconhecido>', gol=0):
    """
    -> Recebe o nome de um jogador e o número de gols e decolve um frase.
    :param jog: Nome do jogador. def=<desconhecido>
    :param gol: Número de gols. def=0
    :return: Frase com os parâmentros.
    """
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
