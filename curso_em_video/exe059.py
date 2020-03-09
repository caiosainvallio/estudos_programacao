"""Exercício criado por : https://www.cursoemvideo.com/
058 Crie um prograam que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em casa caso."""


opcao = ''
while opcao != 5:
    print('\n\nInicio do programa:')
    num_um = int(input('Digite o primeiro valor: '))
    num_dois = int(input('Digite o segundo valor: '))
    opcao = int(input('O que deseja fazer?\n'
                      '[1] somar\n'
                      '[2] multiplicar\n'
                      '[3] maior\n'
                      '[4] novos números\n'
                      '[5] sair do programa\n'))
    if opcao == 1:
        print('Resultado da soma entre {} e {} é {}'.format(num_um, num_dois, num_um + num_dois))
    elif opcao == 2:
        print('Resulatado da multiplicação de {} e {} é {}.'.format(num_um, num_dois, num_um * num_dois))
    elif opcao == 3:
        print('O valor maior é {}.'.format(num_um if num_um > num_dois else num_dois))
    elif opcao == 4:
        continue
    elif opcao == 5:
        break
    else:
        print('Opção não encontrada, começe novamente.')
print('Fim do programa.')
