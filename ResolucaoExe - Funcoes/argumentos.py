'''
1. Faça um programa, com uma função que necessite de três
argumentos, e que forneça a soma desses três argumentos.

'''

def soma_tres_numeros(a, b, c):
    return a + b + c

# Exemplo de uso da função
num1 = 5
num2 = 10
num3 = 15
resultado = soma_tres_numeros(num1, num2, num3)

print(f"A soma de {num1}, {num2} e {num3} é {resultado}")