# Exercício - sistema de perguntas e respostas


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

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta']) #isso exibe o enunciado de cada pergunta
    print()

    opcoes = pergunta['Opções']  #isto é uma lista com as opções disponíveis para o usuário ver na tela do PC.
    for i, opcao in enumerate(opcoes): #exibição das opções e índices de cada opção da lista - usando o enumerate.
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit(): #se o usuário digitou algo em 'escolha' que seja um número inteiro sem pontos...
        escolha_int = int(escolha) #transformar escolha em um número inteiro.

    if escolha_int is not None: #se escolha_int é um numero inteiro que o usuário digitou...
        if escolha_int >= 0 and escolha_int < qtd_opcoes: #se escolha_int é um indice que existe dentro da lista 'opcoes'...
            if opcoes[escolha_int] == pergunta['Resposta']: #vamos comparar: o usuário acertou a resposta? se sim, isso acontece:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')