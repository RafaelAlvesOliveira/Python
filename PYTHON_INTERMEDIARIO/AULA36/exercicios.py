"""
1 — Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""


def saudacao(msg='Olá', nome='usuário'):
    print(msg, nome)


saudacao('Oi', 'Rafael')
saudacao(msg='Hello', nome='João')

"""
2 — Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
"""


def soma(n1=0, n2=0, n3=0):
    somar = n1 + n2 + n3
    return somar


somando = soma(3, 5, 2)
print(somando)

"""
3 — Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado do 
aumento do percentual do mesmo.
"""


def calc(v1, p1):
    perc = v1 + (v1 * (p1 / 100))
    return perc


calc_perc = calc(25, 10)
print(calc_perc)

"""
4 — Fizz Buzz — Se o parâmetro da função for divisível por 2, retorne fizz, se o
parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da função for
divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado.
"""


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'Fizzbuzz'
    if num % 5 == 0:
        return 'Buzz'
    if num % 3 == 0:
        return 'Fizz'
    return num


print(fizzbuzz(7))
