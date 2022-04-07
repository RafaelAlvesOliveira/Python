"""
* Enumerate - Enumerar elementos da lista # list
"""

lista = [
    #  0      1       2
    ['Edu', 'João', 'Luiz'],  # 0
    ['Maria', 'Aline', 'Joana'],  # 1
    ['Ed', 'Helena', 'Lu']  # 2
]

for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2, nome3)
    print(nome1, nome3)
