"""Exercício criado por: https://www.cursoemvideo.com/
102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor
lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo
do fatorial."""


def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opconal) Moatrar ou não a conta. def=False
    :return: O valor do fatorioal de um número n.
    """
    fact = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end=' ')
        fact *= c
    return fact


print('-'*30)
print(fatorial(5))
print('-'*30)
print(fatorial(5, show=True))
