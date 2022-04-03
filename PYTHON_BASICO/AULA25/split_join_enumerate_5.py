"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
*Enumerate - Enumerar elementos da lista # list / iteráveis
"""

# A função "enumerate" enumera elementos de uma lista

string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])
