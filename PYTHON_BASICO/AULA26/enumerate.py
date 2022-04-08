"""
* Enumerate - Enumerar elementos da lista # list
"""

# Lista é um conjunto de elementos, e cada elemento
# contém um índice especifíco que o identifica na lista.
# Um conjunto de elementos pode ser contido de outro conjunto
# de elementos.


lista = [
    #  0      1       2
    ['Edu', 'João', 'Luiz'],  # 0
    ['Maria', 'Aline', 'Joana'],  # 1
    ['Ed', 'Helena', 'Lu']  # 2
]

print(lista[2])
print(lista[1][2])

# Para pegar valores nas listas internas ou lista filhas
# é necessário primeiro indicar qual o índice que
# corresponde a lista e depois o outro índice dentro dela.
