"""
Desempacotamento de listas e  Python
"""

lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

*outra_lista, ultimo_da_lista, n1, n2, n3 = lista

print(ultimo_da_lista)
print(outra_lista, n1, n2, n3)

# A variável '*outra_lista', armazena os valores iniciais
# da lista, as variáveis 'n1', 'n2', 'n3' armazenam os
# três últimos
