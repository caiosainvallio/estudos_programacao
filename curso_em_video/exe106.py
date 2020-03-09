"""Exercício criado por: https://www.cursoemvideo.com/
106: Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário
digitar a palavra 'FIM', o programa se encerrará. Importante: use cores."""


from time import sleep
c = ('\33[m',          # 0 = sem cor
     '\33[0:30:41m',   # 1 = vermelho
     '\33[0:30:42m',   # 2 = verde
     '\33[7:30m',      # 3 = invertido
     '\33[0:30:44m',    # 4 = azul
     )


def ajuda(com):
    print(c[3], end='')
    help(com)
    print(c[0], end='')
    sleep(0.5)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(0.5)


comnando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO', 1)
        break
    else:
        titulo(f'Acessando o manual do comando\'{comando}\'', 4)
        ajuda(comando)
