"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de Ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO -s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 1
# se as chaves não forem incluídas é mostrado o nome da variável em vez
# de ser mostrado o valor contido nela
print(f'{num_1:0>10}')
# Nesse caso é acrescentado o valor zero antes do valor de num_1
# no caso seriam 10 casas, mas são nove zeros acrescentados antes
# do valor contido na variável num_1

num_2 = 1150
# São acrescentados números zero antes do valor contido na variável num_2
# pois o sinal é menor que (<)
print(f'{num_2:0<10}')

num_3 = 9587
# Quando é usado o sinal de circunflexo indica que o valor deve ficar no
# centro, e que serão acrescentados outros valores antes e depois
print(f'{num_3:0^10}')
