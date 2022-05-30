"""
Expressões Lambda ou funções anônimas
"""

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8]
]

lista.sort(key=lambda item: item[1], reverse=True)
# lista.sort(key=lambda item: item[1])
print(lista)

# Essa é outra forma de listar sem ser
# necessário criar uma função para isso.
