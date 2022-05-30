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

# Faz a mesma coisa que a função anterior, e pode-se
# usar os mesmo argumentos para se listar.

print(sorted(lista, key=lambda i: i[1]))
print(sorted(lista, key=lambda i: i[0], reverse=True))
print(lista)


# Outra forma de listar é usando a função sorted, e incluir
# a lista a ser ordenada dentro de parentêses.
