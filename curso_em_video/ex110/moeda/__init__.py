def metade(n=0, formato=False):
    res = n / 2
    return res if not formato else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if not formato else moeda(res)


def aumentar(n=0, p=0, formato=False):
    res = (n * p / 100) + n
    return res if not formato else moeda(res)


def diminuir(n=0, p=0, formato=False):
    res = n - (n * p / 100)
    return res if not formato else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


def resumo(n=0, a=0, d=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analizado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{a}% de aumento: \t\t{aumentar(n, a, True)}')
    print(f'{d}% de redução: \t\t{diminuir(n, d, True)}')
    print('-'*30)
