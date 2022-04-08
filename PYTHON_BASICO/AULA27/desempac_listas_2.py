"""
Desempacotamento de listas e  Python
"""

lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

n1, n2, n3, *outra_lista, ultimo_da_lista = lista


print(ultimo_da_lista)
print(n1, n2, n3, outra_lista)

# A variável 'ultimo_da_lista' serve para armazenar o valor
# do último componente da lista.
