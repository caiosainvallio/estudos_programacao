"""Exercício criado por : https://www.cursoemvideo.com/
008 Escreva um programa que leia um valor em metros e o
exiba convertido em centímetros e milímetros"""


n = float(input('Uma distância em metros: '))
print('A medida de {:.1f}m corresponde a'.format(n))
print('{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(n/1000, n/100, n/10, int(n*10), int(n*100), int(n*1000)))
