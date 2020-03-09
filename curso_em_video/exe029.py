"""Exercício criado por : https://www.cursoemvideo.com/
029 Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostr uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite."""


vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você excedeu a velocidade limite em {}km, você irá pagar uma multa de R${:.2f}'.format(vel - 80, multa))
else:
    print('Você está dentro da velocidade limite, continue assim.')
