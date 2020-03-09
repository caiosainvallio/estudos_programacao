seg = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = seg // 86400
horas = (seg % 86400) // 3600
minu = ((seg % 86400) % 3600) // 60
segs = ((seg % 86400) % 3600) % 60

print(f'{dias} dias, {horas} horas, {minu} minutos e {segs} segundos.')