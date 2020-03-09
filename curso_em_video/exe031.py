"""Exercício criado por : https://www.cursoemvideo.com/
031 Desenvolva um programa que pergunte a distância de uma viagem em km.

Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
e R$0,45 para viagens mais longas."""

dis = int(input('Digite a distância da vigem: '))

if dis <= 200:
    valor = dis * 0.5
else:
    valor = dis * 0.45

print('Para uma viagem de {}km, sua passagem custará R${:.2f}'.format(dis, valor))


"""
Outra forma de fazer a condição:

teste = dis * 0.5 if dis <= 200 else dis * 0.45
"""
