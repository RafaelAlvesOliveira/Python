"""
Classes - Python Orientado a objetos
"""

from pessoa_1 import Pessoa

p1 = Pessoa('Rafael', 31)
p2 = Pessoa('João', 32)

# print(p1.ano_atual)
# print(p2.ano_atual)
# print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
