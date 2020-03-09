"""Exercício criado por: https://www.cursoemvideo.com/
114: Crie um código em Python que teste se o site pudim está
acessível pelo computador usado."""


import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('O site pudim não está acessível no momento.')
else:
    print('Consegui acessar o site pudim com sucesso.')
