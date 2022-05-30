"""
Problemas dos parâmetros mutáveis em funções
"""

# Objetos mutáveis são listas e dicionários
# Objetos imutáveis são tuplas, ‘strings’, números, booleanos, none


def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


lista_clientes_1 = ['Fabrício']
clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'], lista_clientes_1)
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['José', 'Joana', 'Zumira'])

print(clientes1)
print(clientes2)
print(clientes3)
