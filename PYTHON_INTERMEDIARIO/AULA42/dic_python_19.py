"""
Dicionários em Python
"""

# Para se criar uma cópia de um mmódulo real
# é necessário importar o módulo 'copy'
import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Rafael', 'Joana']}
v = copy.deepcopy(d1)
# o comando 'deepcopy' é usado para copiar o dicionário d1.
# Os dois dicionários são independentes um do outro.

v[1] = 'Rafael'
v['d'][0] = 'Joãozinho'
# Quando se usa o símbolo de igual (=) não se faz
# uma cópia, mas sim usando o primeiro como referência.

print(d1)
print(v)

# 'Shallow copy' é quando se altera um determinado
# índice nesse caso na chave 'd'

# Se houver um dicionário dentro de outro, ele poderá ser
# alterado, se for uma tupla não será alterado.
