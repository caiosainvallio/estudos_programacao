"""Exercício criado por : https://www.cursoemvideo.com/
063 Escreva um programa que leia um numero n inteiro qualquer
e mostre na tela os n primeiros elementos de uma Sequância de Fibonacci."""


n = int(input( "Digite o número de elementos da sequência de Fibonacci que deseja ver: "))
if n == 1:
    fib = [0]
elif n == 2:
    fib = [0, 1]
elif n >= 3:
    c = 0
    fib = [0, 1]
    while c < n - 2:
        fib.append(fib[-1] + fib[-2])
        c += 1
print(fib)
