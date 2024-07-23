'''
5. Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h

'''

print('Bem vindo ao Calcula viagem')
distancia_viagem = float(input('Quanto tempo irá levar sua viagem hoje?'))


# Velocidades dos meios de transporte em km/h
velocidade_aviao = 600
velocidade_carro = 100
velocidade_onibus = 80

# Calcula o tempo de viagem para cada meio de transporte
tempo_aviao = distancia_viagem / velocidade_aviao
tempo_carro = distancia_viagem / velocidade_carro
tempo_onibus = distancia_viagem / velocidade_onibus


# Exibe o tempo de viagem para cada meio de transporte
print(f'O tempo de viagem de avião é de: {tempo_aviao:.2f} horas')
print(f'O tempo de viagem de carro é de: {tempo_carro:.2f} horas')
print(f'O tempo de viagem de ônibus é de: {tempo_onibus:.2f} horas')