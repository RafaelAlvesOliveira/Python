"""
    Composição — Python Orientado a objetos
"""

# Composição é a relação mais forte entre classes, nesse
# caso uma classe é dona de objetos de outra classe. Se a
# classe principal for apagada todos os objetos que ela
# utilizou serão apagados com ela.

from classes import Cliente, Endereco

cliente1 = Cliente('Rafael', 31)
cliente1.insere_endereco('São Paulo', 'SP')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('Belo Horizonte', 'MG')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()

print('###############################################')

# O código foi executado, e após ser usado o 'coletor de lixo'
# do Python apagou as informações.
