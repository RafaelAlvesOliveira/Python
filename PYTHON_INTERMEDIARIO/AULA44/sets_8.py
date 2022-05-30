# Add (adicional), update (atualiza), clear, discar
# union | (une)
# Intersection & (todos os elementos presentes nos dois sets)
# difference - Elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

s1 = {1, 2, 3, 4, 5, 7}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 - s2
# Nessa condição só aparecerá o valor '7'
s3 = s2 - s1
# Já nessa condição só aparecerá o valor '6'
# Se usar o sinal de '-' o interpretador só pegara os sinais da esquerda. Nesse
# caso, é necessário ter um elemento que não esteja nos dois 'sets', mas esteja
# no elemento da esquerda

print(s3)

