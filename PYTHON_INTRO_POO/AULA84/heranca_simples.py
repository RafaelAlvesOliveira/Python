"""
    Herança Simples — Python Orientado a objetos
    Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""


from classes import *

# Não é recomendável fazer a importação de todas as classes
# de uma vez, mas nessa aula isso foi necessário. Sempre
# importar o que será usado.

c1 = Cliente('Rafael', 32)
# print(c1.nome)
c1.falar()
c1.comprar()

a1 = Aluno('Maria', 54)
# print(a1.nome)
a1.falar()
a1.estudar()

p1 = Pessoa('João', 43)
p1.falar()


