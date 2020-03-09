"""Exercício criado por : https://www.cursoemvideo.com/
011 Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pint-a-la,
sabendo que cada litro de tinta, pinta uma área de 2m2"""


l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m2.'.format(l, a, l*a))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(l*a*0.5))
