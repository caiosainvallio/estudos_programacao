num = 6532
iterador = 0
digito = 0
soma = 0
tamanho = len(str(num))

while iterador < tamanho:
	digito = num % 10
	num = num // 10
	soma += digito
	iterador += 1

print(f'A soma final é : {soma}')
