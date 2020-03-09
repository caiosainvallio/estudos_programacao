"""Exercício criado por : https://www.cursoemvideo.com/
024 Crie um programa q  ue leia o neme de uma cidade e
diga se ela começa ou não com o nome SANTO"""


city = input('Digite o nome da sua cidade: ').strip()
s = city.upper().split()[0]
if 'SANTO' == s:
    print('Sua cidade possui Santo')
else:
    print('Sua cidade não possui Santo')
