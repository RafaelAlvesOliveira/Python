# Módulos padrão do Python:
# Módulos são arquivos .py (que contém código python) e servem para expandir
# as funcionalidades padrão da linguagem.
# Veja todos os módulos padrão do Python em:
# https://docs.python.org/3/py-modindex.html

from random import *

# O asteriso significa que se quer importar tudo.
# Fazer dessa forma dificulta saber o que será
# importado. Isso também aumenta as possibilidades
# de sobrescrever outras funçõs que estão dentro
# do módulo.


for i in range(10):
    print(randint(0, 10))



