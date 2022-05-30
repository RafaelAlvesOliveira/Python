"""
Try, except — Tratamento de exceções em Python
"""


try:
    print(a)
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')

# Nesse caso pode ser informado um outra exceção para
# um caso atípico.

print('Bora continuar...')



