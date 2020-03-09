num = int(input('Digite o valor de n: '))
i = 0
div = 1
while i < num:
	if div % 2 != 0:
		print(div)
		i += 1
	div += 1
