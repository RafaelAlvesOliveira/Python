"""
Criar, ler, escrever e apagar arquivos
"""

# https://docs.python.org/3/library/functions.html#open


# Foi solicitado ao python que abrisse esse arquivo
# e fosse possível escrever nele ('w'), o sinal de
# ('+') quer dizer que é para ler e escrever nesse
# arquivo.

file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

# A função 'file.write' serve para escrever algo.

file.seek(0, 0)
# É necessário passar dois parâmetros, o primeiro é 'offset'
# que corresponde a posição, e o segundo é 'wheance' sendo
#  a relatividade de onde se procura.
print('Lendo linhas:')
print(file.read())

print('##########')

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

# O 'file.readline' serve para ler cada linha, e o 'end' é para
# informar o interpretador do python que ele não deve quebrar
# uma linha ao final de cada frase.

print('##########')

file.seek(0, 0)
# print(file.readlines())

for linha in file.readlines():
    print(linha, end='')

print('##########')

# Há duas quebras de linha uma do print e a outra da própria
# quebra de linha inserida no texto. Para corrigir é necessário
# colocar o 'end' no final da frase.

for linha in file:
    print(linha, end='')

file.close()
