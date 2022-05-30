"""
Funções - 'def' em Python (Parte 1)
"""


def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, nome)


saudacao()
saudacao(nome='Zezinho', msg='Hi')
saudacao('Olá', 'Rafael Alves')
saudacao('Oi', 'Luiz')
saudacao('Hi', 'Mariana')
saudacao('Olá', 'Otávio')
saudacao('Hello', 'João')

# Se essa mensagem for executada sem nenhum parâmetro
# será apresentado um erro na tela.
# Podem ser usados argumentos nomeados, e nesse caso
# a ordem não altera o resultado.
