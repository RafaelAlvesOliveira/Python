"""
Try, except — Tratamento de exceções em Python
"""


try:
    a = {}  # variável foi alterada de array para dicionário
    print(a[1])
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
# Se preferir posso tratar duas exceções na mesma 'except',
# deve ser usada uma tupla e informar as exceções a serem
# tratadas.
except Exception as erro:
    print('Ocorreu um erro inesperado.')


print('Bora continuar...')



