"""
Zip - Unindo Iteráveis
Zip_longest - Itertools
"""

# Código
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Porto Velho']

# Código
estados = ['SP', 'MG', 'BA', 'RO']

cidades_estados = zip(cidades, estados)

for valor in cidades_estados:
    print(valor[0], valor[1])



