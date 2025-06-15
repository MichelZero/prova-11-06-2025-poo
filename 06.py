

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