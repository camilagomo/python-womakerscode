#If / Else

numero = int(input('Digite seu numero: '))
if numero > 0: #Condição: Número para ser positivo tem que ser maior que zero
    print('Numero é positivo')
else:
    print('Número é negativo!')

# While
numero = -1
while numero < 0: 
    numero = int(input('Digite seu numero: '))

    print("Numero positivo inserido com sucesso!")

# FOR
frutas = ['Maçã', 'Banana', 'Uva'] #declarando uma lista
for fruta in frutas: # para cada
    print(fruta)
