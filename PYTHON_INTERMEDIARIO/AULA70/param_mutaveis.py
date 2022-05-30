"""
Problemas dos parâmetros mutáveis em funções
"""

# Objetos mutáveis são listas e dicionários
# Objetos imutáveis são tuplas, ‘strings’, números, booleanos, none


def lista_de_clientes(clientes_iteravel, lista=[]):
    lista.extend(clientes_iteravel)
    return lista


# O problema é que as duas listas foram unidas automaticamente


clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['José', 'Joana', 'Zumira'])

print(clientes1)
print(clientes2)

# A ideia dessa função é unir as duas listas
# Quando o interpretador do python detecta uma função
# ele avalia isso apenas uma vez, a cada vez que ele
# chamar a função se eu não incluir uma nova lista
# ele usará a lista padrão que consta na função.
