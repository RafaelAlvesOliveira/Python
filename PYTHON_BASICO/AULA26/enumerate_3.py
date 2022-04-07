"""
* Enumerate - Enumerar elementos da lista # list
"""

lista = [
    #  0      1       2
    ['Edu', 'João', 'Luiz'],  # 0
    ['Maria', 'Aline', 'Joana'],  # 1
    ['Ed', 'Helena', 'Lu']  # 2
]

for v1, v2 in enumerate(lista, 53):
    print(v1, v2)


