'''
1. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como ""Suspeita"", 
entre 3 e 4 como ""Cúmplice"" e 5 como ""Assassino"".
Caso contrário, ele será classificado como""Inocente"".
'''

# Lista de perguntas
perguntas = [
    'Telefonou para a vítima?',
    'Esteve no local do crime?',
    'Mora perto da vítima?',
    'Devia para a vítima?',
    'Já trabalhou com a vítima?'
]

# Inicializando o contador de respostas positivas
respostas_positivas = 0

# Fazendo as perguntas e contando as respostas positivas
for pergunta in perguntas:
    resposta = input(pergunta + ' (responda com sim ou não): ').strip().lower()
    if resposta == 'sim':
        respostas_positivas += 1

# Mapeamento do número de respostas positivas para a classificação
classificacao_dict = {
    2: 'Suspeita',
    3: 'Cúmplice',
    4: 'Cúmplice',
    5: 'Assassino'
}

# Obtendo a classificação
classificacao = classificacao_dict.get(respostas_positivas, 'Inocente')

print(f'A classificação da pessoa é: {classificacao}')

'''
Explicação do código
Lista de perguntas: A lista perguntas contém as cinco perguntas sobre o crime.
Inicialização do contador: respostas_positivas é inicializada com 0 para contar quantas respostas "sim" a pessoa deu.
Loop para fazer as perguntas: O loop for itera sobre cada pergunta na lista e pede ao usuário para responder com "sim" ou "não".
Contagem das respostas positivas: Se a resposta for "sim" (ignorando maiúsculas e espaços em branco), incrementa o contador respostas_positivas.
Mapeamento de classificação: O dicionário classificacao_dict mapeia o número de respostas positivas para a classificação correspondente.
Obtendo a classificação: A função get do dicionário retorna a classificação correspondente ao número de respostas positivas ou "Inocente" se o número não estiver no dicionário.
'''
