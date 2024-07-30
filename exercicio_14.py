# Exercícios com funções

#Exercício 01:
# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

#Resolução do Exercício 01:
def multiplica (*args):
    multiplicacao = 1
    for numero in args:
        multiplicacao = multiplicacao*numero
    return multiplicacao
operacao_1 = multiplica(1, 2, 3)
print(f'O valor da multiplicação desejada é igual a {operacao_1}')

#Exercício 02:
# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

#Resolução do Exercício 02:
def par_impar(numero):
    if numero % 2 == 0: #Se o numero é multiplo de 2, ele é par
        return f'{numero} é Par'
    else: #se o número não é multiplo de 2, ele é impar
        return f'{numero} é Ímpar'
multiplo = par_impar(2)
print(multiplo)
