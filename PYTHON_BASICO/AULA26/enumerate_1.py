"""
* Enumerate - Enumerar elementos da lista # list
"""

lista = [
    #  0      1       2
    ['Edu', 'João', 'Luiz'],  # 0
    ['Maria', 'Aline', 'Joana'],  # 1
    ['Ed', 'Helena', 'Lu']  # 2
]

enumerada = enumerate(lista)
print(list(enumerada))

"""
[    0   1
    (0, ['Edu', 'João', 'Luiz']), 
    (1, ['Maria', 'Aline', 'Joana']), 
    (2, ['Ed', 'Helena', 'Lu'])
]
"""
