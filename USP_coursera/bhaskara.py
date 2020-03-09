a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

delta = (b**2 - 4*a*c)

if delta < 0:
	print('esta equação não possui raízes reais')
elif delta == 0:
	raiz = ((-b) / (2*a))
	print(f'a raiz desta equação é {raiz}')
else:
	raiz_um =   ((- b + (delta**(1/2))) / (2*a))
	raiz_dois = ((- b - (delta**(1/2))) / (2*a))
	if raiz_um < raiz_dois:
		print(f'as raízes da equação são {raiz_um} e {raiz_dois}')
	else:
		print(f'as raízes da equação são {raiz_dois} e {raiz_um}')
