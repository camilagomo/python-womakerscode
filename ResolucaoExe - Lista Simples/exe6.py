'''
6. Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).

'''

#Solicitando peso e altura

peso = float(input('Quantos kg você pesa?'))
altura = float (input('Qual a sua altura?'))

IMC = peso / (altura ** 2)

print(f'O seu IMC é de {IMC:.2f}')
