"""Exercício criado por : https://www.cursoemvideo.com/
058 Melhore o jogo do EXE 028 usando while"""
import random


print("Olá, qual o seu nome?")
nome = input()
print("Legal " + nome + ", eu estou pensando em um número entre 1 e 20, tente acertar!")
numeroSecrto = random.randint(1, 20)
for chutes in range(1, 7):
    try:
        print("Chute um número: ")
        chute = int(input())
        if chute < numeroSecrto:
            print("Seu chute foi muito baixo.")
        elif chute > numeroSecrto:
            print("Seu chute foi muito alto.")
        else:
            break  # essa é a condição correta!!
    except ValueError:
        print("Tente escrever um número!")
if chute == numeroSecrto:
    print("Muito bem " + nome + "! Você acertou o número que eu estava pensando com " + str(chutes) + " chutes!")
else:
    print("Não, o número que eu estava pensando era o " + str(numeroSecrto) + ".")
