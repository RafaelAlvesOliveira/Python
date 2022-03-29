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

num_1 = 10
num_2 = 3
divisao = num_1/num_2

nome = 'Rafael Alves'
# para indicar para o interpretador do python que essa variável é
# é uma string, colocasse o s após o símbolo de dois pontos (:).
print(f'{nome:s}')
