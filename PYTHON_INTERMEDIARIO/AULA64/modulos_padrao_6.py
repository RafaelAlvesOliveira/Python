# Módulos padrão do Python:
# Módulos são arquivos .py (que contém código python) e servem para expandir
# as funcionalidades padrão da linguagem.
# Veja todos os módulos padrão do Python em:
# https://docs.python.org/3/py-modindex.html

from random import randint


def randint2(*args):
    return 'hahaha'

# a função 'randint' pode ser renomeada para
# 'randint2' para que não sobrescreva a
# função a que foi importada.


for i in range(10):
    print(randint(0, 10))


