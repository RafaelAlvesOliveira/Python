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
print(f'{num_1:0>10}')

# num_2 = float(1150)
num_2 = 1150
# Existem duas formas de fazer o 'casting' num número
# inteiro para ele ser convertido em float
print(f'{num_2:.2f}')
# Também é possível combinar vários formatos de edição de números
print(f'{num_2:0>10.2f}')
