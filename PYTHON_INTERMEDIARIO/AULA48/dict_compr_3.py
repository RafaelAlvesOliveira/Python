"""
Dictionary Comprehension em Python - (Compreensão de dicionários)
"""

lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d1 = {x.upper(): y.upper() for x, y in lista}
print(d1)
