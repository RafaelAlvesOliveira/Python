"""
Criar, ler, escrever e apagar arquivos
"""

# https://docs.python.org/3/library/functions.html#open

# É usada a função with e depois usar a função 'open'
# para abrir o arquivo da forma que quiser, e depois
# é usado 'as' para criar um apelido para o arquivo.

with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    print(file.read())

# Esse gerenciador de contexto do python, irá abri o arquivo
# e assim que terminar de executar, fecha o arquivo.

