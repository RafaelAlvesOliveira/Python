"""
Dictionary Comprehension em Python - (Compreensão de dicionários)
"""

lista = [
    ('chave', 2),
    ('chave2', 'valor2'),
]

d1 = {x: y*2 for x, y in lista}
print(d1)
