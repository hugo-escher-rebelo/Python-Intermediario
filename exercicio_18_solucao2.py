# Exercícios

# 1) Exercício 01:
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda) e coloque os novos valores dos preços 
#na variável 'novos_produtos'.
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#Minha Solução: Usar LIST COMPREHENSION
novos_produtos = [
    {           #Para cada novo dicionário dentro da lista 'novos-produtos'...
    'nome': produto['nome'],         #manteremos os nomes iguais
    'preco': round(produto['preco']*1.10, 2)   #e o preço é 10% maior que o original
    #Usamos a função round(valor, número de casas decimais) para arredondar o preço dos produtos.
    }           #Fechando cada novo dicionário.
    for produto in produtos 
    ]

#Exibindo a resposta do exercício 01:
print('\nA Solução do Exercício 01 é:\n\n')
print(f'A lista "Novos_Produtos" é:\n')

#print(*novos_produtos, sep='\n') faz o mesmo que essas duas linhas de código abaixo:
for produto in novos_produtos:
    print(produto)

#2) Exercício 02:
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
#e coloque os produtos ordenados na variável 'produtos_ordenados_por_nome'
print('\n\nA Solução do Exercício 02 é:\n')

#Criando uma Deepcopy da lista original:
import copy
nomes_crescentes = copy.deepcopy(novos_produtos)

#Definindo a função que ordena por nome:
def ordenar_nome(dicionario):
    return dicionario['nome']

#Ordenando os dicionários contidos na lista 'nomes_crescentes' pelos nomes de maneira crescente:
nomes_crescentes.sort(key=ordenar_nome)


#Exibindo a lista 'nomes_crescentes' ordenada pelos nomes em ordem crescente:
print(f'\nA lista "Novos_Produtos" ordenada de maneira crescente por NOMES é:\n')
for produto in nomes_crescentes:
    print(produto)

#E como ordenar esta lista em ordem decrescente?

#Criando uma Deepcopy da lista original:
nomes_decrescentes = copy.deepcopy(novos_produtos)

#Ordenando esta lista em ordem decrescente pelos nomes:
nomes_decrescentes.sort(key=ordenar_nome,reverse=True) 


#Exibindo a lista 'nomes_decrescentes' ordenada pelos nomes em ordem decrescente:
print(f'\nA lista "Novos_Produtos" ordenada de maneira decrescente por NOMES é:\n')
for produto in nomes_decrescentes:
    print(produto)

#3) Exercício 03:
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
#e coloque os produtos ordenados na variável 'produtos_ordenados_por_preco'
print('\n\nA Solução do Exercício 03 é:\n')

#Criando uma Deepcopy da nova lista original:
precos_crescentes = copy.deepcopy(novos_produtos)

#Definindo a função que ordena por preço:
def ordenar_preco(dicionario):
    return dicionario['preco']

#Ordenando os dicionários contidos na lista 'novos_produtos' pelos preços de maneira crescente:
precos_crescentes.sort(key=ordenar_preco)

#Exibindo a lista 'precos_crescentes' ordenada pelos preços em ordem crescente:
print(f'\nA lista "Novos_Produtos" ordenada de maneira crescente por preços é:\n')
for produto in precos_crescentes:
    print(produto)


#Fim do programa.