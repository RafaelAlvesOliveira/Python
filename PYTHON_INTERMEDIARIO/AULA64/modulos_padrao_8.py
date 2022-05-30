# Módulos padrão do Python:
# Módulos são arquivos .py (que contém código python) e servem para expandir
# as funcionalidades padrão da linguagem.
# Veja todos os módulos padrão do Python em:
# https://docs.python.org/3/py-modindex.html

import random

# Quando se importa diretamente o módulo, não
# se sobrescreve a primeira função 'randint'.


def randint(*args):
    return 'hahaha'


for i in range(10):
    print(random.randint(0, 10))



