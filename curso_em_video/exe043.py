"""Exercício criado por : https://www.cursoemvideo.com/
043 Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
* Abaixo de 18.5: Abaixo do peso
* Entre 18.5 e 25: Peso ideal
* 25 até 30: Sobrepeso
* 30 até 40: Obesidade
* Acima de 40: Obesidade mórbida"""


peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / (altura * altura)
if imc <= 18.5:
    print('IMC: {:.1f}\nStatus: Abaixo do peso.'.format(imc))
elif imc <= 25:
    print('IMC: {:.1f}\nStatus: Peso ideal.'.format(imc))
elif imc <= 30:
    print('IMC: {:.1f}\nStatus: Sobrepeso.'.format(imc))
elif imc <= 40:
    print('IMC: {:.1f}\nStatus: Obesidade'.format(imc))
else:
    print('IMC: {:.1f}\nStatus: Obesidade mórbida'.format(imc))
