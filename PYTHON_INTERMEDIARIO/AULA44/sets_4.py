# Add (adicional), update (atualiza), clear, discar
# union | (une)
# Intersection & (todos os elementos presentes nos dois sets)
# difference - Elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

s1 = set()
s1.update('a')
s1.update('Python')
s1.update([1, 2, 3, 4, 5], {5, 6, 7, 8})
# É semelhante à função 'add', a diferença é que ela itera sobre o elemento.
# Os 'sets' não respeitam ordem, pode ser que a cada vez que a função for
# executada ele apareça numa ordem específica diferente da que tenha criado.
# 'Sets' não aceitam elementos duplicados.

print(s1)
