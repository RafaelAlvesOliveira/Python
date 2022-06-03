"""
Classes - Python Orientado a objetos
"""

# Quando faz uma instância de uma classe, cria-se um objeto
# a partir de uma classe, ou seja, está se usando um molde
# para criar uma pessoa. Cada pessoa criada nesse molde é
# única e independente

from pessoa import Pessoa

p1 = Pessoa()

# Essa instância, o objeto p1 que é uma pessoa, tem uma variável
# chama nome, que pertence apenas a esse objeto. Nesse caso estou
# criando um atributo da pessoa p1 é o mesmo que uma variável só
# que só para essa objeto.

p2 = Pessoa()

# Se quiser que a p2 tenha um nome, é necessário configurar ela
# lhe atribuindo um nome. Para previnir o erro informado abaixo.

p1.nome = 'Rafael'
p2.nome = 'João'

# Se a função print for usada dessa forma 'print(p2.nome)' apresentará
# um erro de atributo. Quer dizer que variáveis de classe são chamadas
# de atributos da classe.

# É possível criar uma variável que pertença a apenas uma
# pessoa.

