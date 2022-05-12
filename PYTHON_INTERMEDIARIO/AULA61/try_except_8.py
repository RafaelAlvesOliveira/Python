"""
Try, except — Tratamento de exceções em Python
"""


try:
    a = 1/0
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    pass
finally:
    a = None

print(a)

# Mesmo ocorrendo o tratamento de erros, o
# interpretador apresenta um erro que deveria
# ter sido tratado. Sendo assim, é possível
# atribuir um valor padrão para a variável.



