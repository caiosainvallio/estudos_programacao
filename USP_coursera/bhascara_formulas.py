a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

def delta(a, b, c):
	delta = (b**2 - 4*a*c)
	return delta

def raiz_unica(a, b):
	raiz = ((-b) / (2*a))
	return raiz

def raiz_pos(a, b, delta):
	r =((- b + (delta**(1/2))) / (2*a))
	return r

def raiz_neg(a, b, delta):
	r =((- b - (delta**(1/2))) / (2*a))
	return r

delta = delta(a, b, c)


if delta < 0:
	print('esta equação não possui raízes reais')
elif delta == 0:
	raiz = raiz_unica(a, b)
	print(f'a raiz desta equação é {raiz}')
else:
	raiz_um = raiz_pos(a, b, delta)
	raiz_dois = raiz_neg(a, b, delta)
	if raiz_um < raiz_dois:
		print(f'as raízes da equação são {raiz_um} e {raiz_dois}')
	else:
		print(f'as raízes da equação são {raiz_dois} e {raiz_um}')
