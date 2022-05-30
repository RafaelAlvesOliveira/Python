"""
Dicionários em Python
"""

d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla',
}

d1['naoexiste'] = 'Agora existe.'
if 'naoexiste' in d1:
    print(d1['naoexiste'])

print('OI')
