# Atividade Prática 06 - Questão 1
#
# Crie um programa que gera uma senha aleatória com caracteres especiais,
# permitindo que o usuário defina a quantidade de caracteres.
#
# -----------------------------------------------------------------

import random
import string

def gerar_senha(tamanho):
    """
    Gera uma senha aleatória com base no tamanho informado.
    A senha inclui letras (maiúsculas e minúsculas), números e caracteres especiais.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

# Exemplo resolvido:
tamanho_exemplo = 12
senha_exemplo = gerar_senha(tamanho_exemplo)

print("Exemplo resolvido:")
print(f"Senha de {tamanho_exemplo} caracteres: {senha_exemplo}")
print("-" * 20)

# Código interativo:
try:
    print("Opção para testar outros valores:")
    tamanho_novo = int(input("Digite a quantidade de caracteres para a senha: "))
    senha_nova = gerar_senha(tamanho_novo)
    print(f"Sua nova senha é: {senha_nova}")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
