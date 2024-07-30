# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

#Resolução:
#Teste: fazendo um número ser multiplicado por 2 de maneira simples, com o CLOSURE.
def multiplicacao (fator):
    def multiplicar (numero):
        return fator*numero
    return multiplicar
duplicar = multiplicacao (2) #salvei o fator a ser utilizado na minha conta
numero = float(input('Insira um número com casas decimais aqui:')) #inseri o número a multiplicar por 2 na conta
print(duplicar(numero)) #falta executar a função duplicar: esta função precisa do argumento NÚMERO, logo: duplicar(numero) = 2*numero

#Resolução de verdade:
def multiplicacao (fator):
    def multiplicar (numero):
        return fator*numero
    return multiplicar
fatores = 2,3,4 #eu já tenho os fatores para usar na minha conta, porém estão em uma tupla.
condicao = True #criando uma condição que será sempre verdadeira até que não seja mais.
while condicao is True:
    numero = float(input('Insira um número com casas decimais aqui:')) #inseri o número a multiplicar por 2,3,4 na conta
    for fator in fatores: #vou criar as funções duplicar, triplicar e quadruplicar para CADA NÚMERO INSERIDO.
        conta1 = multiplicacao(fator) #EX: duplicar = multiplicacao (2)
        print(f'A multiplicação de {fator} por {numero} é : {conta1(numero)}') #e aqui, no final, adiciono o número que foi inserido.
    acao = input('Deseja multiplicar mais algum número por 2, 3 e 4? [S]im ou [N]ão? R: ')
    acao_final = acao.lower() #Sim vira 'sim' e Não vira 'não'.
    if acao_final.startswith('s') is True: #Se eu quero multiplicar outro número, então:
        continue
    else: #caso eu queira terminar a execução do programa...
        #condicao = False 
        break #essa linha tem o mesmo efeito de condicao = False


