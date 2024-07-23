'''
4. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21

'''

# Função para calcular a conversão
def calcular_conversao(carteira):
    # Dicionário com as taxas de conversão
    taxas_de_conversao = {
        "Dólar Americano": 4.91,
        "Peso Argentino": 0.02,
        "Dólar Australiano": 3.18,
        "Dólar Canadense": 3.64,
        "Franco Suiço": 0.42,
        "Euro": 5.36,
        "Libra Esterlina": 6.21
    }

    # Dicionário para armazenar os resultados da conversão
    conversao = {}

    # Loop através do dicionário de taxas de conversão
    for moeda, taxa in taxas_de_conversao.items():
        # Calcula quanto dinheiro da moeda estrangeira pode ser comprado
        conversao[moeda] = carteira / taxa

    return conversao

# Solicita ao usuário a quantidade de dinheiro na carteira
dinheiro_carteira = float(input("Digite quanto dinheiro você tem na carteira (em R$): "))

# Calcula a conversão
resultado_conversao = calcular_conversao(dinheiro_carteira)

# Exibe os resultados
print("\nCom R$ {:.2f}, você pode comprar:".format(dinheiro_carteira))
for moeda, quantidade in resultado_convers
