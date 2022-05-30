"""
Try, except — Tratamento de exceções em Python
"""


try:
    a = []
    print(a[1])
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except IndexError as erro:
    print('Erro de índice.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')

# Para os casos de erro de 'index' a segunda 'except'
# vai tratar.

print('Bora continuar...')



