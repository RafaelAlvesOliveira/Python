# Módulos padrão do Python:
# Módulos são arquivos .py (que contém código python) e servem para expandir
# as funcionalidades padrão da linguagem.
# Veja todos os módulos padrão do Python em:
# https://docs.python.org/3/py-modindex.html

from random import randint


def randint(*args):
    return 'hahaha'
# Essa função sobrescreveu a função randint, isso
# quer dizer que em algum momento do meu código
# foi informado ao interpretador do Python que a
# função seria reescrita. Sendo assim, em vez de
# o interpretador usar a função importada ele
# usa a que foi criada.


for i in range(10):
    print(randint(0, 10))

# O problema de importar apenas uma função de um
# módulo é que ela pode ser sobrescrita se o
# programa for muito grande.

