num = input('Digite um número inteiro: ')
i = 0
iguais = False
while i < len(num)-1 and not iguais:
	dig_ant = num[i]
	dig_pos = num[i+1]
	if dig_ant == dig_pos:
		iguais = True
	i += 1

if iguais:
	print('sim')
else:
	print('não')