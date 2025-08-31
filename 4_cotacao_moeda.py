# Atividade Prática 06 - Questão 4
#
# Crie um programa que consulte a cotação atual de uma moeda estrangeira
# em relação ao Real Brasileiro (BRL) usando a API da AwesomeAPI.
#
# -----------------------------------------------------------------

import requests
import json

def consultar_cotacao(moeda_origem):
    """
    Consulta a cotação da moeda desejada em relação ao BRL.
    """
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_origem}-BRL"
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        chave = f"{moeda_origem.upper()}BRL"
        if chave in dados:
            cotacao = dados[chave]
            return cotacao
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
        return None

# Exemplo resolvido (Dólar Americano - USD):
print("Exemplo resolvido (USD):")
cotacao_exemplo = consultar_cotacao("USD")
if cotacao_exemplo:
    print(f"Moeda: {cotacao_exemplo['name']}")
    print(f"Valor atual: R$ {float(cotacao_exemplo['bid']):.2f}")
    print(f"Valor máximo: R$ {float(cotacao_exemplo['high']):.2f}")
    print(f"Valor mínimo: R$ {float(cotacao_exemplo['low']):.2f}")
    print(f"Última atualização: {cotacao_exemplo['create_date']}")
else:
    print("Moeda não encontrada ou erro na consulta.")
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
moeda_nova = input("Digite o código da moeda (ex: USD, EUR, BTC): ")
cotacao_nova = consultar_cotacao(moeda_nova)
if cotacao_nova:
    print(f"Moeda: {cotacao_nova['name']}")
    print(f"Valor atual: R$ {float(cotacao_nova['bid']):.2f}")
    print(f"Valor máximo: R$ {float(cotacao_nova['high']):.2f}")
    print(f"Valor mínimo: R$ {float(cotacao_nova['low']):.2f}")
    print(f"Última atualização: {cotacao_nova['create_date']}")
else:
    print("Moeda não encontrada ou erro na consulta.")
