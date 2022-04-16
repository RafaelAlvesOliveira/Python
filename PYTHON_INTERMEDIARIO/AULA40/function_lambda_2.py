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


def func(item):
    return item[1]

# Nesse caso o interpretador lista conforme
# os preços, por ser informado o valor 1
# do 'array' de preços.


lista.sort(key=func)
print(lista)
