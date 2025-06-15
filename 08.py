

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
    pessoas[nome] = idade

# Encontra a pessoa mais velha
mais_velha = None
idade_maxima = -1  # Inicializa com um valor muito baixo

for nome, idade in pessoas.items():
    if idade > idade_maxima:
        idade_maxima = idade
        mais_velha = nome

# Encontra a pessoa mais nova
mais_nova = None
idade_minima = float('inf')  # Inicializa com um valor muito alto

for nome, idade in pessoas.items():
    if idade < idade_minima:
        idade_minima = idade
        mais_nova = nome

# Imprime os resultados
print("\nPessoa mais velha:", mais_velha, "com", idade_maxima, "anos")
print("Pessoa mais nova:", mais_nova, "com", idade_minima, "anos")