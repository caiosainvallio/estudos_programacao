"""Exercício criado por : https://www.cursoemvideo.com/
018 Faça um programa que leia um ângulo qualquer e mostre na
tela o valor do seno, cosseno e tangente desse ângulo."""
from math import sin, cos, tan, radians


a = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, sin(radians(a))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, cos(radians(a))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(a, tan(radians(a))))

# Obs. para usar o sin, cos, tan tive de transformar em radiano antes.
