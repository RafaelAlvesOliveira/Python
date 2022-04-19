"""
Dicionários em Python
"""

# Para criar dicionários com chaves, podesse usar qualquer
# dado que seja imutável. Geralmente 'strings'.
d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla',
}

print(d1[(1, 2, 3, 4)])
