"""
Dicionários em Python
"""

d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla',
}

d1.update({'nova_chave': 'novo_valor'})
# Outra forma de atualizar dados no dicionário
# é usando o comando update. Ela contém outro
# dicionário conta um par de chave e valor

if d1.get('str') is not None:
    print(d1.get('str'))

print(123)
