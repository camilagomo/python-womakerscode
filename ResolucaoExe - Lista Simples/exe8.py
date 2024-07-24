'''
8. Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.

'''

# Solicita ao usuário o número de horas de exercício físico por semana
horas_exercicio = float(input("Digite o número de horas de exercício físico por semana: "))

# Calcula o número total de minutos de exercício por semana
minutos_por_semana = horas_exercicio * 60

# Calcula as calorias queimadas por semana
calorias_por_minuto = 5
calorias_por_semana = minutos_por_semana * calorias_por_minuto

# Calcula as calorias queimadas em um mês (considerando 4 semanas em um mês)
calorias_por_mes = calorias_por_semana * 4

# Exibe o resultado
print(f"Você queimará aproximadamente {calorias_por_mes:.2f} calorias em um mês.")
