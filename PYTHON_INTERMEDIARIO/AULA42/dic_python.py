"""
Dicionários em Python
"""

# São muito semelhantes às listas, tem um índice
# e um valor, A diferença entre os dicionários e as listas
# é que o python gera um índice dependendo de quantos
# elementos há nela. E no caso do dicionário é possível
# controlar os índices, é uma estrutura que suporta um par
# de chave e valor.

d1 = {'chave1': 'valor da chave'}
d1['nova_chave'] = 'Valor da nova chave'

print(d1['chave1'])
# Para acessar apenas uma das chaves, é só informar o índice
# da mesma entre colchetes na função print
