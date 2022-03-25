"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseada na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Rafael'
idade = 32
altura = 1.8
peso = 81
ano_atual = 2022
ano_nasc = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}.')
print(f'O IMC de {nome} é {imc}')
print(f'{nome} nasceu em {ano_nasc}')
