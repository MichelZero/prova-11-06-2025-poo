

# Construção de Dicionário a Partir de Listas: Crie um programa 
# em Python que receba duas listas: uma lista de nomes e uma 
# lista de e-mails (assuma que as listas têm o mesmo tamanho e 
# que a ordem corresponde). Use essas listas para criar um 
# dicionário onde o nome seja a chave e o e-mail seja o valor. 
# Imprima o dicionário resultante.

nomes = ["DAvi", "Dani", "pedro"]
emails = ["davi@example.com", "dani@example.com", "pedro@example.com"]

# Inicializa um dicionário vazio
dicionario_emails = {}

# Verifica se as listas têm o mesmo tamanho
if len(nomes) != len(emails):
  print("Erro: As listas de nomes e e-mails devem ter o mesmo tamanho.")
else:
  # Itera sobre as listas usando um loop for e o índice
  for i in range(len(nomes)):
    # Adiciona cada nome como chave e o e-mail correspondente como valor
    dicionario_emails[nomes[i]] = emails[i]

  # Imprime o dicionário resultante
  print("Dicionário de e-mails:")
  print(dicionario_emails)
  
  '''
  Como o código funciona:
Inicialização:
nomes = ["Alice", "Bob", "Charlie"] e emails = ["alice@example.com", "bob@example.com", "charlie@example.com"]: Define as listas de nomes e e-mails.
dicionario_emails = {}: Cria um dicionário vazio para armazenar o resultado.
Verificação de Tamanho:
if len(nomes) != len(emails):: Verifica se as listas têm o mesmo número de elementos. Se não tiverem, imprime uma mensagem de erro e encerra a execução do restante do código.
Iteração e Construção do Dicionário:
for i in range(len(nomes)):: Inicia um loop for que itera sobre os índices da lista nomes (poderia ser emails também, já que as duas tem o mesmo tamanho, garantido pela verificação anterior). range(len(nomes)) gera uma sequência de números de 0 até o comprimento da lista nomes menos 1.
dicionario_emails[nomes[i]] = emails[i]: Dentro do loop, esta linha faz o trabalho principal:
nomes[i]: Acessa o nome no índice i da lista nomes.
emails[i]: Acessa o email no índice i da lista emails.
dicionario_emails[nomes[i]] = emails[i]: Atribui o e-mail (emails[i]) ao nome (nomes[i]) como um par chave-valor no dicionário dicionario_emails.
Impressão do Dicionário:
print("Dicionário de e-mails:") e print(dicionario_emails): Imprime o dicionário resultante no console.
  '''