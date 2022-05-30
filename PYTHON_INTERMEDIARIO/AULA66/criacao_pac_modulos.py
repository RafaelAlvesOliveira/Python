"""
Criação de pacotes e módulos
"""


# import vendas.calc_precos
# from vendas import calc_precos
from vendas.calc_precos import aumento, reducao
# from formata.formataPreco import real
import formata.formataPreco as formato

# São três maneiras de importar funções em
# outros pacotes no arquivo python


preco = 49.90
# preco_com_aumento = vendas.calc_precos.aumento(valor=preco, porcentagem=15)
# preco_com_aumento = calc_precos.aumento(valor=preco, porcentagem=15)
preco_com_aumento = aumento(valor=preco, porcentagem=15, formata=True)
print(preco_com_aumento)

# Essas três linhas correspondem respectivamente a cada uma
# das importações acima. Em cada método de importação a função
# é escrita de uma forma diferente.


preco_com_reducao = reducao(valor=preco, porcentagem=15, formata=True)
print(preco_com_reducao)

print(formato.real(50))

# P.S.: Não foi possível fazer usando subpasta, tive que colocar a
# pasta formata no mesmo nível da pasta vendas para conseguir a
# correta execução do processo explicado em aula.

