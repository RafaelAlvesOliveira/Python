"""
    Classes Abstratas - Python orientado a objetos
"""

# Será criado um sistema de contas bancárias, a conta não
# poderá ser instanciada, mas a classe conta será especializada
# como conta-corrente, conta poupança, conta universitária e
# assim por diante.

from classes.cc import ContaCorrente
from classes.cp import ContaPoupanca

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)

print('##########################')
cc = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)
