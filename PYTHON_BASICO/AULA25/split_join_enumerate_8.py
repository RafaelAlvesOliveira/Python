"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
*Enumerate - Enumerar elementos da lista # list / iteráveis
"""
lista = ['Rafael', 'João', 'Maria']

for indice, nome in enumerate(lista):
    print(indice, nome)

# A diferença desta lista para a anterior é que
# não tem uma lista dentro de outra, mas pode-se
# obter os índices da mesma forma, através do
# comando enumerate.
