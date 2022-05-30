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

# Se quiser inverter a ordem é só colocar
# o comando 'reverse' recebendo o valor 'True'.
# Lista os produtos mais caros para os mais baratos.


lista.sort(key=func, reverse=True)
print(lista)
