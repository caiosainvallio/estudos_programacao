"""Exercício criado por : https://www.cursoemvideo.com/
040 Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
* Média abaixo de 5.0: REPROVADO
* Média entre 5.0 e 6.9: RECUPERADO
* Média 7.0 ou superior: APROVADO"""


n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2
if media < 5:
    print('Média: {:.1f}\nStatus: \033[1:31mREPROVADO\033[m.'.format(media))
elif media < 7:
    print('Média: {:.1f}\nStatus: \033[1:33mRECUPERAÇÃO\033[m.'.format(media))
else:
    print('Média: {:.1f}\nStatus: \033[1:32mAPROVADO\033[m.'.format(media))
