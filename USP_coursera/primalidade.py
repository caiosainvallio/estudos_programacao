num = int(input('Digite um número inteiro: '))
i = 1
div = 0

while i <= num:
	if num % i == 0:
		div += 1
	i += 1

if div == 2:
	print('primo')
else:
	print('não primo')
