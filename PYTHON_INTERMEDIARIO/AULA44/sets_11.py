# Add (adicional), update (atualiza), clear, discar
# union | (une)
# Intersection & (todos os elementos presentes nos dois sets)
# difference - Elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

l1 = ['Rafael', 'Luiz', 'Maria']
l2 = ['Rafael', 'Luiz', 'Luiz', 'Luiz', 'Maria', 'Maria']

l1 = list(set(l1))
l2 = list(set(l2))
# Pode se converter de lista para 'set' e após volta para lista.
# Isso pode ser feito sem comprometer a lista original

print(l1, l2)
