""""
Tipos de dados
str - string - textos 'Assim' "Assim"
int - inteiro - 123456 0 -10 -20 -50 -60 -15000 1500
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico - True/False 10 == 10
"""
# Type casting é o método para converter um certo tipo de dado em
# outro, para executar uma determinada operação seja executada pelo
# usuário.
# Tirando valores como string vazia, zero, zero de ponto flutuante,
# dicionário vazio, coisas que estão vazias são avaliadas em false.
# Se for qualquer valor diferente desse ele considera como verdadeiro.
print('Rafael', type('Rafael'), bool('Rafael'))

# Exemplo de type casting por fazer a conversão de uma string em um int.
print('10', type('10'), type(int('10')))

# O python não permite converter textos para inteiros
# print('rafael', int('rafael'))

# Também não permite converter um número de ponto flutuante
# para inteior
# print('rafael', int('10.5'))

# Se a string for um número decimal, é possível fazer a conversão
print('rafael', float('10.5'))

# Também é possível converter um número inteiro em float
print('rafael', float('10'))
