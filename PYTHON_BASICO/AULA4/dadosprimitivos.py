""""
Tipos de dados
str - string - textos 'Assim' "Assim"
int - inteiro - 123456 0 -10 -20 -50 -60 -15000 1500
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico - True/False 10 == 10
"""
# A função type vai retornar o tipo de valor da variável
print('Rafael', type('Rafael'))

# Se qualquer valor numérico for colocado dentro de aspas
# o interpretador, vai considerá-lo como string
# Sem as aspas é considerado um inteiro ou int
print(10, type(10))


# Valores numéricos decimais são interpretados como sendo
# do tipo float, se estiver dentro de aspas será considerado
# como sendo uma string
print(25.23, type(25.23))

# Os caracteres '==' servem para fazer uma comparação entre
# dois valores para ver se ambos são iguais, se forem iguais
# retornará o valor booleano true, senão será false.
print(10 == 10, type(10 == 10))

# O interpretador do python sabe diferenciar entre maiúsculas
# e minúsculas
print('l' == 'L', type('l' == 'L'))

# strings vazias são consideradas como sendo valor booleano false
print('', type(''))

# Em todos esses casos o interpretador sempre avaliará como falso
print(bool(''))
print(bool([]))
print(bool(0))
