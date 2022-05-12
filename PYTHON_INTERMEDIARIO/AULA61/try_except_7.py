"""
Try, except — Tratamento de exceções em Python
"""


try:
    # a = 1/0
    a = {}
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    print('Seu código foi executado com sucesso!')
    print(a)
finally:
    print('Finalmente!')

print('Bora continuar...')

# Diferente do bloco 'else' o bloco 'finally'
# sempre será executado. Independente de haver
# algum erro em algum trecho do código.



