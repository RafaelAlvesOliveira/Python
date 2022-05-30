"""
Try, except — Tratamento de exceções em Python
"""

# É muito similar ao 'if' e 'else' a diferença
# é que nesse caso são tratadas exceções.

try:
    a = 0
    try:
        a = 1/0
    except:
        print('Erro')
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    pass
finally:
    a = ''

print(a)

# O primeiro bloco 'try' tem outro bloco 'try'
# dentro dele e isso não permite que a exceção
# se propague para o outro bloco 'try.

