'''
4. Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l.
'''

# Litros de combustível e distância

litro = float(input('Litros de combustível?'))
distancia = float(input('Qual distância percorrida?'))

# Calcula o consumo médio em km/l
media = distancia / litro 

print(f'O KM/L em consumo medio é de {media:.2f} km/l') 


