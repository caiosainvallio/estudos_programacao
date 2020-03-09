n = int(input('Digite o valor de n: '))
k = int(input('Digite o valor de k: '))

def fatorial(num):
	fat = 1
	i = 1
	while i <= num: 
		fat *= i
		i += 1
	return fat

def binomial(n, k):
	Cnk = fatorial(n)/(fatorial(k)*fatorial(n - k))
	return Cnk

print(binomial(n, k))
