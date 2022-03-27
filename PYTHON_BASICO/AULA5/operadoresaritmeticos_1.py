""""
+, -, *, /, //, **, %, ()
"""

# Se for feita a multiplicação de duas strings o python
# apresentará um erro
# print('Multiplicação * ', 10 * 10)

# Mas se for feita a multiplicação entre uma string e um
# inteiro faz com que o sinal * se torne um operador de
# repetição
print('Multiplicação * ', 10 * '10')
print('Multiplicação * ', 10 * 'rafael')

# Se for dois valores inteiros, serão somados
print('Adição +', 5 + 5)
# Caso sejam duas strings serão concatenadas
print('Adição +', '5' + '5')
# Se for fazer uma operação entre string e inteiro
# será gerado um erro informadno que o operando
# não funciona nessa situação
print('Adição +', 5 + '5')

print('Rafael' + ' ' + 'Alves e ele tem ' + '31' + ' anos')
# O sinal de mais pode ser usado para concatenar várias
# strings, e se porventura houver um valor inteiro, pode
# ser convertido usando um tipo primitivo
print('Rafael' + ' ' + 'Alves e ele tem ' + str(31) + ' anos')
