"""
Desempacotamento de listas e  Python
"""

lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

n1, n2, n3, *outra_lista = lista

print(n1, n2)
print(n1, n2, n3, outra_lista)

# Se for declarado um número menor de variáveis do que
# existe na lista o interpretador apresntará um erro
# informando que tem mais valores a serem desempacotados

# Para solucionar esse problema, pode se incluir uma
# variável com * na frente para indicar que o restante
# dos valores fazem parte de outra lista.
