# Add (adicional), update (atualiza), clear, discar
# union | (une)
# Intersection & (todos os elementos presentes nos dois sets)
# difference - Elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

l1 = ['Rafael', 'Luiz', 'Maria']
l2 = ['Rafael', 'Luiz', 'Luiz', 'Luiz', 'Maria', 'Maria']

if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')