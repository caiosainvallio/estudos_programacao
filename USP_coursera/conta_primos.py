def primo(num):
	i = 1
	div = 0

	while i <= num:
		if num % i == 0:
			div += 1
		i += 1

	if div == 2:
		r = True
	else:
		r = False
	return r

def n_primos(num):
	i = 1
	soma = 0
	while i <= num:
		if primo(i):
			soma += 1
		i += 1
	return soma
