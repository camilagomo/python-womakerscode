# O que são listas

lista_frutas = [] #declaração da lista
lista_frutas.append('Maça')
lista_frutas.append('Uva')
print(lista_frutas)

#Caso queira interpretar o usuário digitando
fruta = input('Digite sua fruta: ')
lista_frutas.append(fruta)

#Tuplas
tupla = ('Maça', 'Banana', 'Uva', 'Melão')
print (tupla)

#Dicionarios 
dicionario = {'Chave':'Valor'}
dicionario['maca'] = 'É uma fruta'
dicionario['carro'] = 'É um veículo'
dicionario['Gato'] = 'É um animal'
print(dicionario)