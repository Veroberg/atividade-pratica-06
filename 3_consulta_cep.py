# Atividade Prática 06 - Questão 3
#
# Desenvolva um programa que consulte informações de endereço a partir
# de um CEP fornecido pelo usuário, utilizando a API ViaCEP.
#
# -----------------------------------------------------------------

import requests
import json

def consultar_cep(cep):
    """
    Consulta a API ViaCEP e retorna as informações de endereço.
    """
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        if 'erro' not in dados:
            return dados
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
        return None

# Exemplo resolvido:
print("Exemplo resolvido (CEP 01001-000):")
dados_exemplo = consultar_cep("01001000")
if dados_exemplo:
    print(f"Logradouro: {dados_exemplo['logradouro']}")
    print(f"Bairro: {dados_exemplo['bairro']}")
    print(f"Cidade: {dados_exemplo['localidade']}")
    print(f"Estado: {dados_exemplo['uf']}")
else:
    print("CEP não encontrado ou inválido.")
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
cep_novo = input("Digite o CEP (apenas números): ")
dados_novo = consultar_cep(cep_novo.replace('-', '').replace('.', ''))
if dados_novo:
    print(f"Logradouro: {dados_novo['logradouro']}")
    print(f"Bairro: {dados_novo['bairro']}")
    print(f"Cidade: {dados_novo['localidade']}")
    print(f"Estado: {dados_novo['uf']}")
else:
    print("CEP não encontrado ou inválido.")
