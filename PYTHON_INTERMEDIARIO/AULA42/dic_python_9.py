"""
Dicionários em Python
"""

d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla',
}

del d1['str']
# O comando 'del' é usado para apagar a chave
# e o valor de 'str'.
print(d1)

