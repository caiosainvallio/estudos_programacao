num = str(input('Digite um número inteiro: '))

print(f'O dígito das dezenas é {num[-2] if len(num) > 1 else 0}')