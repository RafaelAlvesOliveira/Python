"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
*Enumerate - Enumerar elementos da lista # list / iteráveis
"""

string = " O Brasil é o país do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print(lista_2)

for valor in lista_1:
    print(valor)

# Cada iteração aparecerá numa linha diferente e separada
# por espaço.

