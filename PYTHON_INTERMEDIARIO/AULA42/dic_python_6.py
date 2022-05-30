"""
Dicionários em Python
"""

d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla',
}

d1['nomedachave'] = 'Agora ela existe'
if d1.get('nomedachave') is not None:
    print(d1.get('nomedachave'))

print(123)
