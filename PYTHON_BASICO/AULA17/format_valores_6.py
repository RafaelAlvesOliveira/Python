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
nome_formatado = '{n:0<20}'.format(n=nome)
# é possível nomear uma determinada variável
# na função format
print(nome_formatado)
