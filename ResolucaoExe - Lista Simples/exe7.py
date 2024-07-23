'''
7. Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.

'''

# Usuário informa quanto ganha por hora
ganha_hora = float(input('Qual o seu valor hora?'))

# Horas trabalhadas no mês
horas_mes = float(input('Neste mês, quantas horas foram trabalhadas?'))

#Total ganho por mês

mes = ganha_hora * horas_mes

print(f'No mês você receberá {mes:.f}')