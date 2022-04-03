"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
*Enumerate - Enumerar elementos da lista # list / iteráveis
"""

string = "O Brasil é o o o país do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista_2:
    print(valor.strip().capitalize())

# A função "strip" serve para retirar os espaços no início e no
# final das frases. A função "capitalize" serve para alterar
# a primeira letra de uma frase de minúscula para maiúscula.

# a função "split" faz a divisão da lista conforme o valor
# informado para se realizar a divisão.
