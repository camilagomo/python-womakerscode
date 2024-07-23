'''
2. Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

'''

# Qual período você estuda?

turno = str(input('Digite M caso o período seja Matutino, V caso seja Vespertino, ou N caso seja Noturno: ')).strip().upper()

# Condição Bom dia, Boa tarde, Boa noite , Valor inválido

if turno == 'M':
    print('Bom dia!')

elif turno == 'V':
    print ('Boa tarde!')

elif turno == 'N':
    print ('Boa noite!')

else: 
    print('Valor inválido!')
    
