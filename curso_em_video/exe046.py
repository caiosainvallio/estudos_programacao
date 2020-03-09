"""Exercício criado por : https://www.cursoemvideo.com/
046 Faca um programa que mostre na tela uma contagem regressiva para o estouro de fogos
de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles."""
from time import sleep

print('Atenção para o top de 10 segundos!')
for i in range(10, 0, -1):
    sleep(1)
    print(i)
print('FELIZ ANO NOVOOO!!!')
