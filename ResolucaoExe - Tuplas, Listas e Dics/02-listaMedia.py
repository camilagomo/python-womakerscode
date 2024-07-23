'''
2. Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0.

'''

# Lista para armazenar as médias dos alunos
medias = []

# Loop para pedir as notas de 5 alunos
for i in range(5):
    print(f'Aluno {i+1}')
    soma_notas = 0
    # Loop para pedir 4 notas de cada aluno
    for j in range(4):
        nota = float(input(f'Digite a nota {j+1}: '))
        soma_notas += nota
    # Calcula a média das notas do aluno
    media = soma_notas / 4
    medias.append(media)

# Contar quantos alunos têm média maior ou igual a 7.0
contagem_alunos_acima_7 = 0
for media in medias:
    if media >= 7.0:
        contagem_alunos_acima_7 += 1

# Imprimir o resultado
print(f'Número de alunos com média maior ou igual a 7.0: {contagem_alunos_acima_7}')
