"""
Operadores Relacionais
== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente
"""

nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')

idade = int(idade)

# Limite para pegar o empréstimo
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo. ')
