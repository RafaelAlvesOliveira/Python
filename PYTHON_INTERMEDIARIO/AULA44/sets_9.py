# Add (adicional), update (atualiza), clear, discar
# union | (une)
# Intersection & (todos os elementos presentes nos dois sets)
# difference - Elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

s1 = {1, 2, 3, 4, 5, 7}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 ^ s2
# Nesse caso é o comando 'intersect' que pega os elementos que aparecem em ambos
# os 'sets', mas não se repetem.

print(s3)

