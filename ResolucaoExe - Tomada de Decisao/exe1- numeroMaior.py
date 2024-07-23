'''
1. Faça um Programa que peça dois números e imprima o maior deles.
'''

# Insirir número

num1 = float(input('Insira um número:'))
num2 = float(input('Insira outro número:'))

print(num1)
print(num2)

#Qual número é maior?

if num1 > num2:
    print(f'O número {num1} é maior que {num2}')
elif num2 > num1:
    print(f'O número {num2} é maior que {num1}')
else:
    print('Os números são iguais')


