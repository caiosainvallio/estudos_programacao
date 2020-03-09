l = int(input('Digite a largura: '))
a = int(input('Digite a altura: '))

i = 1
while i <= a:
	if i == 1 or i == a:
		print('#' * l)
	else:
		print('#' + ' ' * (l-2) + '#')
	i += 1
