"""Exercício criado por: https://www.cursoemvideo.com/
105: Faça um programa que tenha uma função notas() que pode receber várias notas de
alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor."""


def notas(*n, sit=False):
    """
    -> Função para analizar notas e situações de vários alunos.
    :param n: Uma ou mais notas de alunos (aceita mais de uma)
    :param sit: Indica se deve adicioar a situação. def=False
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    cont = 0
    maior = menor = 0
    soma = 0
    boletim = dict()
    for i in n:
        if cont == 0:
            maior = menor = i
        else:
            if i > maior:
                maior = i
            if i < menor:
                menor = i
        soma += i
        cont += 1
    boletim['total'] = cont
    boletim['maior'] = maior
    boletim['menor'] = menor
    media = soma / cont
    boletim['média'] = media
    if sit:
        if media > 7:
            boletim['situação'] = 'BOA'
        elif media > 5:
            boletim['situação'] = 'RAZOAVEL'
        else:
            boletim['situação'] = 'RUIM'
    return boletim


print('-'*30)
resp = notas(6.5, 7, 9, 9, 9, sit=True)
print(resp)
