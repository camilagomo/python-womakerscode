'''
Formas de criar um comentário em python
'''

print('Olá Mundo')

# Tipo INT - INTEIRO
numero = int(input('Digite seu numero:'))
print(numero)

# Tipo float
numero = float(input('Digite um número float:'))
print(numero)

# Tipo textual - string 
frase = input('Digite sua frase:')
print(frase)

'''Por padrão, o tipo textual já é interpretado automaticamente'''

# Operações Matemáticas 
# Soma = +
numero1 = int(input('Digite o numero 01:'))
numero2 = int(input('Digite o numero 02: '))
soma = numero1+numero2
print(soma)

# Sub = -
numero1 = int(input('Digite o numero 01:'))
numero2 = int(input('Digite o numero 02: '))
subtrair = numero1-numero2
print(subtrair)

# Multiplicação
numero1 = int(input('Digite o numero 01:'))
numero2 = int(input('Digite o numero 02: '))
multiplicacao  = numero1*numero2
print(multiplicacao)

# Divisão
numero1 = int(input('Digite o numero 01:'))
numero2 = int(input('Digite o numero 02: '))
divisao = numero1/numero2
print(divisao)

# Divisão Inteira = //
numero1 = int(input('Digite o numero 01:'))
numero2 = int(input('Digite o numero 02: '))
divisao_inteira = numero1//numero2
print(divisao_inteira)

#Resto
10%2
10%3

#Incremento
valor = 5
valor += 1
print(valor)

#decremento
valor = 5
valor -= 1
print(valor)

# Ordem de precedencia 
calculo = (2+5)*((5+4)*3)
print(calculo)

# Operadores relacionais

'''
== : igual
 > : maior
 >= : menor igual
 <  : menor
 <= : menor igual
 != : diferente

'''

#Formatando mensagens
numero1 = int(input('Digite o numero 01:'))
numero2 = int(input('Digite o numero 02: '))
soma = numero1+numero2
print(f'A soma dos número resulta em {soma}')

#str.format
valor = 45.00
print(f'{valor:.2f}') #casas após a vírgula

nome = 'Camila'
print('Olá {}, você tem {} anos'.format('Camila'))