"""
Try, except — Tratamento de exceções em Python
"""


try:
    print(a)
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')

# O código não precisa parar por causa de um erro.
print('Bora continuar...')

# Os erros podem ser salvos em arquivos de 'log', ou
# enviar mensagens ao utilizador informando qual é o
# erro. Nesse último caso isso não é interessante.

