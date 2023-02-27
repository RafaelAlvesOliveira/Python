# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# get

p1 = {
    'nome': 'Rafael',
    'sobrenome': 'Alves'
}
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# O comando get obtém a chave do dicionário e retorna
# o nome ou valor da chave.

# pop

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# O método pop elimina a chave do dicionário, mas a mesma
# pode ser atribuída a uma variável.

# popitem

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# popitem remove a última chave do dicionário.

# update

# p1.update({
#     'nome':'novo nome',
#     'sobrenome': 'novo sobrenome',
#     'idade' : '30'
# })

# p1.update(nome='novo valor', idade='30')

tupla = (('nome', 'novo valor'), ('idade', '30'))
lista = [['nome', 'novo valor'], ['idade', '30']]
p1.update(tupla)
p1.update(tupla)
print(p1)

# O método update atualiza as informações dentro do dicionário,
# e também através dele é possível acrescentar novas informações
# ao dicionário.