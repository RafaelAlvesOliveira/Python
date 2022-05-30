# Módulos padrão do Python:
# Módulos são arquivos .py (que contém código python) e servem para expandir
# as funcionalidades padrão da linguagem.
# Veja todos os módulos padrão do Python em:
# https://docs.python.org/3/py-modindex.html

from random import randint as randint_original

# Se não houver outra opção a não ser usar
# funções no código que tenha o mesmo nome
# da função importada, então pode-se
# criar apelido(s) para elas.


def randint(*args):
    return 'hahaha'


for i in range(10):
    print(randint_original(0, 10))

print(randint())

