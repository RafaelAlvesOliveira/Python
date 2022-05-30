"""
Tuplas
"""
# A tupla pode ser criada sem os parentêses
t1 = 1, 2, 'a', 'b'

print(t1)

# Se não for incluída uma vírgula após o primeiro elemento
# o interpretador do python considera o primeiro valor da
# tupla como sendo um inteiro nesse caso.
t2 = 1,

print(t2, type(t2))
