# Add (adicional), update (atualiza), clear, discar
# union | (une)
# Intersection & (todos os elementos presentes nos dois sets)
# difference - Elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

l1 = ['Rafael', 'Luiz', 'Maria']
l2 = ['Rafael', 'Luiz', 'Luiz', 'Luiz', 'Maria', 'Maria']
# Nessa condição se fossem verificadas ambas as listas,
# receberiam o valor booleano de false.
print(l1 != l2)

l1 = set(l1)
l2 = set(l2)

print(l1 == l2)
# Se fizer 'casting' nas listas e transformá-las em 'set' ambas
# serão consideradas iguais.
