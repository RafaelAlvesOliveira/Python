"""
Criar, ler, escrever e apagar arquivos
"""

# https://docs.python.org/3/library/functions.html#open

# O 'a' indica que serão acrescentadas informações, sem
# necessariamente apagar os que já existem. O cursor é
# colocado no final do arquivo, assim quando for dado o
# comando para se escrever, a informação será inserida
# no final da frase.

with open('abc.txt', 'a+') as file:
    file.write('Outra linha\n')
    file.seek(0)
    print(file.read())

