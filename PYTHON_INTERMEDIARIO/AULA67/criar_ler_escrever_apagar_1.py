"""
Criar, ler, escrever e apagar arquivos
"""

# https://docs.python.org/3/library/functions.html#open

try:
    file = open('abc.txt', 'w+')
    file.write('Linha')
    file.seek(0, 0)
    print(file.read())
finally:
    file.close()

# Essa é uma maneira que muitas pessoas trabalham, mas não
# é a melhor maneira de se trabalhar com arquivos em python.

