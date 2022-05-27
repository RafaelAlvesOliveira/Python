"""
Criar, ler, escrever e apagar arquivos
"""

# https://docs.python.org/3/library/functions.html#open

# O 'r' depois do nome do arquivo, indica que o mesmo
# está apenas sendo lido.

with open('abc.txt', 'r') as file:
    print(file.read())

