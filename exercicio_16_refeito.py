# Exercício - sistema de perguntas e respostas
#Quero simular uma prova: o programa irá mostrar a pergunta, as opções e o usuário irá escrever a resposta (assinalar multipla escolha)
#Aí o programa irá falar se o usuário acertou ou errou cada pergunta
#Ao final do programa, o usuário irá saber a nota dele (acertou quantas? errou quantas?)

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
#Solução 2 do problema:
nota = 0 
for pergunta in perguntas: #para que todas as perguntas sejam exibidas pelo programa:
    print('\n\nPergunta: ',pergunta['Pergunta']) #assim, exibiremos a pergunta de cada problema do teste.
    print('\n\n')

    #Usaremos o método 'enumerate' de listas ou tuplas para exibir mais facilmente as opções de cada pergunta:
    opcoes = pergunta['Opções'] #salvando os valores da chave opcões em uma única lista
    opcoes_enumeradas = enumerate(opcoes) #adicionando indices a cada item da lista: ('Maria', 'João') vira ('0 Maria', '1 João')
    for indice, item in opcoes_enumeradas: #formatando a exibição de cada alternativa da pergunta que o usuário verá na tela;
        print(f'{indice}) {item}')

    #Agora, o usuário irá inserir a resposta dele:
    resposta = input('\n\nInsira o índice da resposta desejada: ')
    #Validando a resposta do usuário:
    validar = resposta.isdigit() #a resposta deve conter apenas NÚMEROS
    if validar is True: #se a resposta do usuário conter apenas números, ou seja, for verdadeira:
        resposta_int = int(resposta) #convertemos a resposta em um número inteiro.
        if resposta_int >=0 and resposta_int < len(opcoes): #verificando se o índice da resposta existe dentro da lista:
            gabarito = pergunta['Resposta']
            if opcoes[resposta_int] == gabarito: #se a resposta assinalada for igual ao gabarito, então acertou!
                nota = nota + 1
                print('\nParabéns, você acertou esta pergunta :) ')
            else: #se errou a pergunta:
                print('\nQue pena: você errou a pergunta :( )')  
        else: #se o indice digitado pelo usuário não está contido nos indices da lista, então...resposta inválida.
            print('\nO índice digitado não existe: A resposta é inválida')
    else: #Se a resposta for inválida, nada é feito e o programa avisa que não pode ter resposta inválida.
        print('\nResposta inválida: sua resposta deve conter apenas números inteiros!')
#Ao final das 3 questões, devo indicar a nota final do usuário:
print(f'\nA sua nota final é {nota} de 3 ')
#Fim da solução do exercício :)