#! python3

"""
Este script retira e-emails dentro de um texto copiado no clipboard
e devolve para o clipboard uma lista de e-mails nao duplicados para 
ser colado em um aruivo de texto/planilha
@caiosainvallio
"""

import re
import pyperclip

# cria uma funcao que acha e-mails em um texto
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+	 # parte do nome
@	             # parte do @
[a-zA-Z0-9_.+]+  # parte do domínio
''', re.VERBOSE)

# carrega um texto do clipboard
texto = pyperclip.paste()

# usa a funcao de extracao de e-mail no texto carregado
emailExtraido = emailRegex.findall(texto)

# cria uma lista com os e-mails
extraido = '\n'.join(emailExtraido) + '\n'

# coloca os e-mails em minusculo
minusculo = extraido.lower()

# transforma em lista para aplicar outra funcao
lista = minusculo.split(sep="\n")

# exclui o ultimo elemento da lista (espaco vaizio "\n")
lista = lista[:-1]

# funcao set patra manter valores unicos (exclui diplicatas)
n_duplicado = set(lista)

# transforma a lista em texto
resultado = "\n".join(map(str, n_duplicado))

# coloca a nova lista d e-mail no clipboard
pyperclip.copy(resultado)

# mensagem final para o uduario
print("Pronto! Agora é só colar em um arquivo de texto.")
