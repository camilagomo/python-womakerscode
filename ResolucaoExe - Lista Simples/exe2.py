'''
2. Peça ao usuário para informar o ano de nascimento. Em seguida,
calcule e imprima a idade atual.
'''

from datetime import datetime

print ('Olá, tudo bem?')
ano_nascimento = int(input('Digite o seu ano de nascimento:'))

ano_atual = datetime.now().year
idade_atual = ano_atual - ano_nascimento

print(f'Sua idade atual é de  {idade_atual}')
