# Atividade Prática 06 - Questão 2
#
# Crie um programa que gera um perfil de usuário aleatório usando a
# API 'Random User Generator' e exibe nome, email e país.
#
# -----------------------------------------------------------------

import requests
import json

def obter_usuario_aleatorio():
    """
    Obtém um perfil de usuário aleatório da API e retorna as informações.
    """
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        return nome, email, pais
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
        return None, None, None

# Exemplo resolvido:
print("Exemplo resolvido:")
nome_exemplo, email_exemplo, pais_exemplo = obter_usuario_aleatorio()
if nome_exemplo:
    print(f"Nome: {nome_exemplo}")
    print(f"Email: {email_exemplo}")
    print(f"País: {pais_exemplo}")
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
input("Pressione Enter para gerar um novo usuário...")
nome_novo, email_novo, pais_novo = obter_usuario_aleatorio()
if nome_novo:
    print(f"Nome: {nome_novo}")
    print(f"Email: {email_novo}")
    print(f"País: {pais_novo}")
