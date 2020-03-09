"""Exercício criado por : https://www.cursoemvideo.com/
037 Escreva um programa que leia um número inteiro qualquer e peça para o
usuário escolher qual será a base de conversão:
[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADECIMAL"""

num = int(input('Digite um número inteiro: '))
print('''Escolha umas das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é agual a {}'.format(num, bin(num)[2:]))
elif opcao ==2:
    print('{} conertido para OCTAR é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.  Tente novamente.')