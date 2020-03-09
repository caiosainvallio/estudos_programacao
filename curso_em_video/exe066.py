"""Exercício criado por : https://www.cursoemvideo.com/
066 Crie um programa que leia vários números inteiros pelo tecalado. O programa só vai parar quando o usuário
digitar o valor 999,  que 'é a condição de parada. No final, mostre quantos números foram digitados e qual
foi a soma entr eles (desconsiderando o flag)"""


n = cont = soma = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitados {cont} números e a soma foi {soma}')
