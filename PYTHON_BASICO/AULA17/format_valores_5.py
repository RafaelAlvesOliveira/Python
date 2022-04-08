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
nome = 'Rafael Alves'
# nome_formatado = '{:@>50}'.format(nome)
nome_formatado = '{:@>12}'.format(nome)
# se forem 12 caracteres eles não apareceram as @, pois, é o
# comprimento do nome informado
print(nome_formatado)
