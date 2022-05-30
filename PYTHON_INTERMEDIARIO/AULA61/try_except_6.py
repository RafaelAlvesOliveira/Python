"""
Try, except — Tratamento de exceções em Python
"""


try:
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

print('Bora continuar...')

# Sempre que o código do bloco 'try' for executado
# sem haver nenhuma exceção, o bloco 'else' é
# executado, caso venha haver algum erro será
# tratado pelas exceções.


