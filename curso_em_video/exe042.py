"""Exercício criado por : https://www.cursoemvideo.com/
042 Refaça o exercício 35 dos triângulos, acrescentendo o
rescurso de mostrar que tipo de triângulo será formado:
* EQUILÁTERO: todos os lados iguais
* ISÓSCELES: dois lados iguais
* ESCALENO: todos os lados diferentes"""


l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 > abs(l2 - l3) and l2 > abs(l1 - l3) and l3 > abs(l1 - l2):
        print('Estes valores fomam um triângulo!')
        if l1 == l2 and l2 == l3:
            print('Este triângulo é EQUILÁTERO.')
        elif l1 == l2 or l2 == l3 or l1 == l3:
            print('Este triângulo é ISÓSCELES.')
        else:
            print('Este triângulo é ESCALENO.')
    else:
        print('Esses valores não fomam um triângulo...')
else:
    print('Esses valores não fomam um triângulo...')
