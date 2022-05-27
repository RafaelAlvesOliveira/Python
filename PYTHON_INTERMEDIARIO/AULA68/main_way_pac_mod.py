try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )
except ImportError:
    raise

# Esse 'template' serve adicionar o caminho completo da
# pasta superior

# from pacote1.modulo1 import variavel1
from pacote2.modulo2 import variavel2

# print(variavel1)
print(variavel2)
print(sys.path)

# O 'sys.path' serve para informar os caminhos
# onde o interpretador do python vai buscar os arquivos.
# Se ele não encontrar o módulo, será apresentado um erro,
# informando que o módulo não existe, com o nome informado.

