# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

#Exercício 01 - Função que duplica o número recebido como parâmetro:
def multiplicar(multiplo): #ex de 'multiplo': 2 --> x2; 3 --> x3; 4 --> x4.
    def realizar_conta(numero): #'numero' é o numero que quero inserir como parâmetro.
        return multiplo*numero  #esse é o resultado final.
    return realizar_conta  #eu quero usar o 'closure' para facilitar a utilização do usuário, ainda que complique o código.
duplicar = multiplicar(2)  #criando a função que duplica um número inserido como parâmetro;
triplicar = multiplicar(3) #criando a função que triplica um número inserido como parâmetro;
quadruplicar = multiplicar(4) #criando a função que quadruplica um número inserido como parâmetro;
numeros = [1,2,3] #produzindo a automatização do processo de introduzir cada número nas trêss funções criadas acimas.
for numero in numeros:
    print(f'Para o número {numero}, temos:')
    print(duplicar(numero)) #realizando o 'closure' da função duplicar, triplicar e quadruplicar, respectivamente.
    print(triplicar(numero))
    print(quadruplicar(numero))
