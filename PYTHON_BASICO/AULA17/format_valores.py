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
# o ponto indica casa decimais, o '2' indica quantas casas depois da vírgula e o 'f' é de float
print('{:.2f}'.format(divisao))
# pode ser feita a mesma coisa usando f "strings"
print( f'{divisao:.2f}')


