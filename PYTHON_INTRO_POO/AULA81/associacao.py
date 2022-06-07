"""
    Associação — Python Orientado a Objetos
"""


from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

# print(escritor.nome)
# print(caneta.marca)
# maquina.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()


# Foi criado o objeto escritor, depois foi criada uma
# caneta e uma máquina de escrever. Foi criado o atributo
# ferramenta, a ferramenta vai receber um objeto inteiro
# da máquina ou da caneta.

# Resumindo: isto significa que posso usar o objeto escritor
# chamar o objeto ferramenta, executar um método que está
# no método caneta ou maquinaDeEscrever.

# Essa é a associação mais fraca que tem, pois, se o escritor
# for apagado os outros dois métodos funcionam independente dele.

