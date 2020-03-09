"""Exercício criado por : https://www.cursoemvideo.com/
069 Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer continuar.
No final, mostre:
a) Quantas pessoas tem mais de 18 anos
b) Quanos homens foram cadastrados
c) Quantas mulheres tem menos de 20 anos"""


print('=' * 8 + ' INÍCIO DO PROGRAMA ' + '=' * 8)
maior = homens = mulheres_20 = 0
while True:
    print('-'*30 + '\nCADASTRE UMA PESSOA\n' + '-'*30)
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    sexo = input('Sexo: [f/m] ').upper()
    while sexo not in 'MF':
        sexo = input('Sexo: [f/m] ').upper()
    if sexo == 'M':
        homens += 1
    if sexo == 'M' and idade < 20:
        mulheres_20 += 1
    continuar = input('Quer continuar? [S/N]').upper()
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]').upper()
    if continuar == 'N':
        break
print('='*8 + ' FIM DO PROGRAMA ' + '='*8)
print(f'Total de pessoas com mais de 18 anos: {maior}')
if homens == 1:
    print('Ao todo temos 1 homem cadastrado.')
elif homens == 0:
    print('Não tivemos homens cadastrados.')
else:
    print(f'Ao todo temos {homens} homens cadastrados')
if mulheres_20 == 1:
    print(f'E temos 1 mulher com menos de 20 anos')
elif mulheres_20 == 0:
    print('Não tivemos mulheres com menos de 20 anos.')
else:
    print(f'E temos {mulheres_20} mulheres com menos de 20 anos.')
