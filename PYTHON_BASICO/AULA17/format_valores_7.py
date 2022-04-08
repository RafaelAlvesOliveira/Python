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
sobrenome = 'Nascimento'

nome_formatado = '{0:$^50} {1:#^50}'.format(nome, sobrenome)
# É possível acessar o índice também, sendo possível
# formatar apenas o índice. Podem ser utilizados diversos
# índices e formatar eles de formas diferentes
print(nome_formatado)
