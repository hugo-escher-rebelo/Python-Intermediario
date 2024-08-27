"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
listas = [
    
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
]

#Solução:
#primeiro_duplicado = -1 #Caso padrão, onde não há numeros duplicados, logo: a resposta é -1.

for lista in listas: #Em cada lista de número, eu quero fazer o seguinte:
    verificacao = set() #criei um set vazio.

    for numero in lista: #Quero ter acesso a todos os numeros individualmente em cada lista.
        
        if numero in verificacao: #será que o numero que eu estou analisando já está no set? Se sim...
            primeiro_duplicado = numero #a resposta do problema vira o numero digitado.
            break #Como não quero mais repetir esse procedimento depois que a primeira repetição aparecer, saio do for...
        else: #se for a primeira vez que ele aparece na lista de números....
            verificacao.add(numero) #Quero adicionar o numero acessado no set criado 'verificacao'...
            primeiro_duplicado = -1



    print(f'\nA Lista analisada é: {lista}\n') #Exibição da lista analisada
    if primeiro_duplicado == -1: #Se não houver números repetidos na lista...
        print('Não há números duplicados nesta lista.')
    else: #Se houver, quero imprimir somente o primeiro número duplicado.
        print(f'E o primeiro número duplicado da mesma é: {primeiro_duplicado}')