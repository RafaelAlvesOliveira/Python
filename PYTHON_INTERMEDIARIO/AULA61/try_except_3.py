"""
Try, except — Tratamento de exceções em Python
"""


try:
    a = []
    print(a[1])
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')

# Foi feita a tentativa de se imprimir um valor que
# não existe e devido a isso foi acionada o segundo
# 'except' sendo para os casos de erro inesperado.

print('Bora continuar...')



