"""Exercício criado por : https://www.cursoemvideo.com/
056 Desnvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
* A média de idade do grupo
* Qual é o nome do homem mais velho
* Quantas mulheres têm menos de 20 anos"""


soma = 0
velho = 0
nome_vei = 'nada'
mulher = 0
for i in range(5):
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = int(input('Sexo:\nMasculino = 1\nFeminino = 2\n'))
    soma += idade
    if sexo == 1 and idade > velho:
        velho = idade
        nome_vei = nome
    if sexo == 2 and idade < 20:
        mulher += 1
print('Média de idade: {:.1f}'.format(soma/5))
if velho == 0:
    print('Não tem homens na lista')
else:
    print('O homem mais vélho com {} anos chama-se {}'.format(velho, nome_vei.title()))

if mulher == 0:
    print('Não tem mulher menor que 20 anos na lista.')
else:
    print('Número de mulheres menores de 20 anos na lista é igual a  {}'.format(mulher))
