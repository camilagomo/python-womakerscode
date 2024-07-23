'''
3. Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.

# Converte quilômetros para metros, centímetros e milímetros

metros = quilometros * 1000
centimetros = metros * 100
milimetros = centimetros * 10

'''

print('Olá, seja bem-vindo!')

# Solicita ao usuário a quantidade de quilômetros percorridos
km_percorridos = float(input('Quantos KM você percorreu hoje? '))

# Converte quilômetros para metros, centímetros e milímetros
metros = km_percorridos * 1000
centimetros = km_percorridos * 100000  # 1 km = 1000 m = 100000 cm
milimetros = km_percorridos * 1000000  # 1 km = 1000 m = 1000000 mm

# Exibe os resultados
print(f'{km_percorridos} quilômetros é igual a:')
print(f'{metros} metros')
print(f'{centimetros} centímetros')
print(f'{milimetros} milímetros')

