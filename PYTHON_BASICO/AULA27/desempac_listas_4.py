"""
Desempacotamento de listas e  Python
"""

lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

n1, n2, *_ = lista

print(n1)

# A variável '*_' se não for necessário usar o restante da lista
# e outros programadores que olharem isso saberão que o restante
# da lista é desnecessário
