"""
Operadores Lógicos
and, or, not
in e not in
"""
# O operador lógico "not" serve para inverter o que o operador in faz, se o parâmetro procura
# dentro de uma determinada variável não existir será considerado verdeiro.

nome = 'Rafael Alves'

if 'ves' not in nome:
    print("Executei.")
else:
    print("Existe o texto.")

