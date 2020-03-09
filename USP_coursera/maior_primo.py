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

def maior_primo(num):
	i = 1
	maior = 0
	while i <= num:
		if primo(i):
			maior = i
		i += 1
	return maior

