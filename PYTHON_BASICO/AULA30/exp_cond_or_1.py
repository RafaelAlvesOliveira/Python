"""
Expressões condicionais com operador OR
"""

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Rafael'

variavel = a or b or c or d or f or g

print(variavel)

# Nessa situação o interpretador do python
# pega o primeiro valor verdadeiro que nesse
# caso é 22. Se os valores g e f estivessem
# invertidos o primeiro valor que apareceria
# seria o nome 'Rafael'.
