#  lists, tuples, str -> Sequences -> Iterável
nome = 'Rafael'

for letra in nome:
    print(letra)


print('#' * 80)

for letra in nome:
    print(letra)

print(nome)

# o comando 'for' converte em tempo de execução
# a minha 'string' em um iterador, porque o 'for'
# vai utilizar o 'next' até o iterador esgotar

# Resumindo o 'for' converte a variável nome para
# iterador em tempo de execução e depois utilizará
# o 'next'. Quando chegar no fim do iterador, se o
# 'next' for chamado novamente uma exceção será
# levantada 'Stop Iteration', apresentará um erro
# devido a ter terminado o iterador. Terminando o
# primeiro for, ele vai para o próximo trecho de
# código.
