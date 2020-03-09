a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

delta = (b**2 - 4*a*c)

if delta < 0:
	print('Esta equação não possui raízes reais')
elif delta == 0:
	raiz = ((-b) / (2*a))
	print(f'A raiz dessa equação é: {raiz}')
else:
	raiz_um =   ((- b + (delta**(1/2))) / (2*a))
	raiz_dois = ((- b - (delta**(1/2))) / (2*a))
	print(f'As raíses da equação são: {raiz_um} e {raiz_dois}')
