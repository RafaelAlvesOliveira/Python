from map_dados import produtos, pessoas, lista


# Cada elemento da lista será multiplicado por dois.

nova_lista = map(lambda x: x * 2, lista)
# Muito similar a 'list comprehension'.
print(lista)
print(list(nova_lista))
# Foi feito o 'casting' para converter o objeto 'map.'
# em uma lista

# A função 'map.' recebe outra função como
# primeiro argumento. A função 'Lambda' será
# usada como primeiro argumento.

