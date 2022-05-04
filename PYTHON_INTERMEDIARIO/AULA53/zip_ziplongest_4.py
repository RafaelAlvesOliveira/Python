"""
Zip - Unindo Iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest
# import itertools

# Código
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Porto Velho', 'Senhor do Bonfim']

# Código
estados = ['SP', 'MG', 'BA', 'RO']

cidades_estados = zip_longest(estados, cidades, fillvalue='Estado')
# cidades_estados = itertools.zip_longest(estados, cidades, fillvalue='Estado')
# Só faria dessa forma, se tivesse importado o módulo itertools
# diretamente sem ter importado especificamente a função 'zip_longest'.
print(list(cidades_estados))
    
# O 'zip_longest' une todas as listas, mas o 'zip' une até
# as listas até encontrar a mais curta, então para.


