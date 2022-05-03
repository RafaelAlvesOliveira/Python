"""
Dictionary Comprehension em Python - (Compreensão de dicionários)
"""

lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d1 = {x: y for x, y in lista}
# d1 = dict(lista)
print(d1)
