"""Exercício criado por : https://www.cursoemvideo.com/
065 Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer
ou não continuar a digitar valores."""


sn = 's'
n = 0
soma = 0
maior = 0
menor = 99999
cont = 0
while sn == 's':
    n = int(input('Digite um valor: '))
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    sn = input('Deseja continuar? [s/n]: ')
    if sn == 's':
        cont += 1
    else:
        break
print('Mádia: {}\nMaior: {}\nMenor: {}'.format(soma/cont, maior, menor))
