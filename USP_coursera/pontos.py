x1_ = int(input('x1: '))
y1_ = int(input('y1: '))

x2_ = int(input('x2: '))
y2_ = int(input('y2: '))

distancia = (((x1_ - x2_)**2) + ((y1_ - y2_)**2)) ** (1/2)

if distancia >= 10:
	print('longe')
else:
	print('perto')
