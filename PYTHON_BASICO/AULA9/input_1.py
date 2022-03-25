"""
Entrada de dados
"""
nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")
ano_nascimento = 2022 - int(idade)

print()
# Esse print() vazio serve como quebra de linha.
print(f'{nome} tem {idade} anos.'
      f' {nome} nasceu em {ano_nascimento}')

