"""
Dicionários em Python
"""

d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla',
}

print('str' in d1)
# Essa confirmação será veradeira, pois existe
# a chave informada no dicionário.
print('str' in d1.keys())
# Esse é igual ao primeiro, como é um valor booleano,
# pode ser usado com 'if' ou 'else'.
print('valor' in d1.values())
# Essa é uma forma de acessar os valores do dicionário.
