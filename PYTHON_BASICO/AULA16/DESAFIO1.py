"""
Faça um programa que peça ao usuário para digiar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um inteiro
"""

# Programa para identificar se o número digitado é ímpar ou par

numero_inteiro = input('Digite um número inteiro: ')

if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)
    if numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} é par')
    else:
        print(f'{numero_inteiro}é ímpar')
else:
    print('Isso não é um número inteiro.')
