

# Crie um programa em Python que receba do usuário o nome e 
# a idade de cinco pessoas. Armazene esses dados em um dicionário, 
# onde o nome seja a chave e a idade seja o valor. 
# Em seguida, imprima o nome da pessoa mais velha e da pessoa mais nova.


# Inicializa o dicionário para armazenar os dados das pessoas
pessoas = {}

# Recebe os dados do usuário para cada pessoa
for i in range(5):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    pessoas[nome] = idade  # Armazena o nome como chave e a idade como valor no dicionário


# Encontra a pessoa mais velha
mais_velha = None # Inicializa com None, pois ainda não sabemos quem é a mais velha
idade_maxima = -1  # Inicializa com um valor muito baixo, para garantir que qualquer idade válida será maior

# percorre o dicionário para encontrar a pessoa mais velha 
for nome, idade in pessoas.items():
    if idade > idade_maxima:
        idade_maxima = idade
        mais_velha = nome

# Encontra a pessoa mais nova
mais_nova = None # Inicializa com None, pois ainda não sabemos quem é a mais nova
idade_minima = float('inf')  # Inicializa com um valor muito alto

# percorre o dicionário para encontrar a pessoa mais nova
for nome, idade in pessoas.items():
    if idade < idade_minima:
        idade_minima = idade
        mais_nova = nome

# Imprime os resultados
print("\nPessoa mais velha:", mais_velha, "com", idade_maxima, "anos")
print("Pessoa mais nova:", mais_nova, "com", idade_minima, "anos")

#################################################################
# opcionalmente, você pode exibir todos os dados coletados
# Exibe os dados coletados
print("\nDados coletados:")
for nome, idade in pessoas.items():
    print(f"{nome}: {idade} anos")