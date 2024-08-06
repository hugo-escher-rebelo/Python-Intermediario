# Exercício - sistema de perguntas e respostas
#Quero simular uma prova: o programa irá mostrar a pergunta, as opções e o usuário irá escrever a resposta (assinalar multipla escolha)
#Aí o programa irá falar se o usuário acertou ou errou cada pergunta
#Ao final do programa, o usuário irá saber a nota dele (acertou quantas? errou quantas?)

#Solução simplificada:
#Este é o teste a ser resolvido pelo usuário: Facilitando a minha vida primeiro - o teste é um dicionário com uma única pergunta.
perguntas = {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    }
#Exibição da pergunta:
print(perguntas['Pergunta'])
#Opções para escolher - exibir:
opcoes = list(perguntas['Opções'])
indice = 0
indice_resposta = 2
for opcao in opcoes:
    print(f'{indice}) {opcao}')
    indice = indice + 1
#Inserindo a resposta do usuário:
resposta = input('Insira o ÍNDICE da resposta: 0) 1 --> Digitar 0 para falar que a resposta é 1: ')
resposta_int = int(resposta)
if perguntas['Opções'][resposta_int] == opcoes[indice_resposta]:
    print('Parabéns, você acertou :)')
else:
    print('Que pena, você errou!')

#Como fazer isso para várias perguntas?
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

#Solução Final:
def transformacao (numero): #essa função retorna uma letra a partir de um número inserido
    letras = ['A', 'B', 'C', 'D']
    letra = letras[numero]
    return letra 
nota = 0
for pergunta in perguntas: #Acessando cada dicionário individualmente
    itens = pergunta.items() #isso ainda não é uma lista ou tupla
    tupla_itens = tuple(itens) #eu não quero alterar os valores, então usarei tupla
    for chave, valor in tupla_itens: #para cada par de chave e valor dentro da tupla...
        if chave == 'Pergunta': #se a chave for 'pergunta'...
            print(valor)        #quero imprimir a pergunta para o usuário ler a pergunta.
        elif chave == 'Opções': #se a chave for 'opções'...
            indice = 0
            for opcao in valor: #vamos exibir as opções para o usuário.
                indice_modificado = transformacao (indice)
                print(f'{indice_modificado}) {opcao}') 
                indice = indice + 1 
        else: #chave == 'Resposta'
            gabarito = int(valor)
    #Agora eu quero que o usuário digite a resposta que ele quer assinalar:   
    resposta = input('Insira a resposta desejada (Não é a letra da resposta, mas sim a resposta diretamente): ')
    resposta_int = int(resposta)
    #Comparar o gabarito (é um número inteiro) com a resposta dada pelo usuário e CALCULAR A NOTA DO USUÁRIO
    if resposta_int == gabarito:
        nota = nota + 1
        print('Parabéns, você acertou!')
    else:
        print('Que pena, você errou :( )')
print(f'A sua nota neste teste é: {nota} de 3')