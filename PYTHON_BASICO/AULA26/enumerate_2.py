"""
* Enumerate - Enumerar elementos da lista # list
"""

lista = [
    #  0      1       2
    ['Edu', 'João', 'Luiz'],  # 0
    ['Maria', 'Aline', 'Joana'],  # 1
    ['Ed', 'Helena', 'Lu']  # 2
]

enumerada = list(enumerate(lista))
print(enumerada[0][0])
print(enumerada[1][1][2])

"""
[    0   1
    (0, ['Edu', 'João', 'Luiz']), 
        0        1       2
    (1, ['Maria', 'Aline', 'Joana']), 
    (2, ['Ed', 'Helena', 'Lu'])
]
"""

# 'Enumerate' serve para enumerar os elementos de uma lista
