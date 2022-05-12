"""
Try, except — Tratamento de exceções em Python
"""

# Para se tratar exceções em python é necessário
# envolver o código dentro do try e except


try:
    print(a)
except NameError as erro:
    print('Error', erro)

# Para se tratar os erros é necessário informar o tipo
# de erro que se quer tratar no 'except'.

