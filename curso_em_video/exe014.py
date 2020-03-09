"""Exercício criado por : https://www.cursoemvideo.com/
014 Escreva um programa que converta uma temperatura
digitada em Ceucius e converta para Fahrenheit."""


temp = float(input('Informe a tempreatura em C: '))
print('A temperatura de {}C corresponde a {}F'.format(temp, 9 * temp / 5 + 32))
