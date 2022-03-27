nome = 'Rafael'
idade = 31  # int
altura = 1.80  #float
e_maior = idade > 18  # bool
peso = 81
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'de idade e seu imc é', imc)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
# Essa é outra maneira de imprimir variáveis na tela usando f string
# Dentro da variável imc no print é possível controlar a quantidade
# de casas decimais para isso é só incluir ":.nºcdf"
# nºcd é a abreviatura para número de casas decimais

print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc))
# "format" é outra forma de imprimir variáveis dentro da função print
# para isso é necessário colocar as variáveis na ordem em que devem aparecer

print('{2} {0} {0} tem {1} anos e seu imc é {2}'.format(nome, idade, imc))
# pode se incluir os índices das variáveis, com isso não é necessário colocar na
# ordem em que foram declaradas, e também pode-se repetir a mesma variável várias vezes.

print('{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))
# Também é possível nomear os parâmetros dentro da função format, e já que eles estão
# nomeados, podem ser colocados em qualquer ordem e/ou repetir as variáveis
