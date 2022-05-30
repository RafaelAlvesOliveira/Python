"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05


0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro dígito = 1 (Se o dígito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67 ##
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo dígito = 0

Novo CNPJ + Dígitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
54329865432 -> Primeiro dígito
6543298765432 -> Segundo dígito
"""

import cnpj


cnpj1 = '71.506.168/0001-11'

if cnpj.valida(cnpj1):
    print(f'{cnpj1} é válido')
else:
    print(f'{cnpj1} é inválido')

