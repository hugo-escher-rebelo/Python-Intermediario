# Exercícios com funções
#Questão 01:
# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
#Questão 01: Sem o usuário poder inserir livremente os dados que quiser - não sei fazer isso ainda.
multiplicacao = 1
def multiplicar (*args):
    global multiplicacao
    for argumento in args:
        multiplicacao = multiplicacao*argumento
    return multiplicacao
multiplicacao_1 = multiplicar (1,2,3) #inseri argumentos na minha função: isso não é uma tupla e os argumentos estão desempacotados.
print(f'A multiplicação dos argumentos inseridos é {multiplicacao_1}')

#Alteração no código: a tupla pré-definida vai ser utilizada para que a multiplicação seja feita:
tupla = 1,2,3,4 #Preciso desempacotar esta tupla antes de executar a função
multiplicacao = 1
def multiplicar (*args): #Aqui eu empacoto novamente: 1, 2 vira (1,2)
    print(args) #verificação: aqui os números da tupla estão empacotados novamente.
    global multiplicacao
    for argumento in args:
        multiplicacao = multiplicacao*argumento
    return multiplicacao
multiplicacao_1 = multiplicar (*tupla) #aqui eu desempacoto a tupla: (1,2) vira 1, 2
print(f'A multiplicação dos argumentos inseridos é {multiplicacao_1}')


#Questão 02:
# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
numero = int(input('Digite um número inteiro aqui:'))
def par_impar(number):
    if number % 2 == 0: #Se o resto da divisão do número inserido é igual a 0
        return f'O número {numero} é Par' #o número é par
    else: #Neste caso, o número é impar
        return f'O número {numero} é Ímpar'
natureza_numero = par_impar(numero)    
print(natureza_numero)
