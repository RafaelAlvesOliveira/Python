"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
*Enumerate - Enumerar elementos da lista # list / iteráveis
"""

string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ','.join(lista)

print(string)
print(lista)
print(string2)

# a função "join" serve para juntar os índices de uma lista
# nesse caso o critério usado para juntá-los é a ",", mas
# poderia ser o espaço, mas poderia ser usado qualquer outro
# caractere.
