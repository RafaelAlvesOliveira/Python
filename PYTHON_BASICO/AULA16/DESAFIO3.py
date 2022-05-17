"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver
4 letras ou menos escreva "o seu nome é curto"; se tiver entre 5 e 6 letras,
escreva "o seu nome é normal"; maior que 6 escreva "o seu nome é muito grande".
"""

# Programa para contar o número de letras do nome de uma pessoa

nome = input('Digite seu primeiro nome ')

tamanho = len(nome)

if tamanho <=4:
    print('Seu nome é muito curto')
elif tamanho <=6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')

