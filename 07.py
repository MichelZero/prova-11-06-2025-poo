

# Escreva um programa em Python que receba uma lista 
# de números como entrada e retorne uma nova lista 
# contendo os mesmos números ordenados em ordem decrescente.
# Você pode usar o método sort() ou a função sorted().
# Explique a diferença entre os dois e qual deles 
# você utilizou e por quê.

numeros = [5, 2, 8, 1, 9, 4]

# Cria uma cópia da lista original para não modificá-la diretamente
numeros_ordenados = numeros[:]  # Usando slicing para criar uma cópia

# Ordena a cópia da lista em ordem decrescente usando o método sort()
numeros_ordenados.sort(reverse=True)

print("Lista original:", numeros)
print("Lista ordenada decrescentemente:", numeros_ordenados)

# Explicação da diferença entre sort() e sorted():

# sort():
# - É um método de lista.
# - Modifica a lista original (in-place).
# - Não retorna nada (None).

# sorted():
# - É uma função built-in do Python.
# - Cria uma nova lista ordenada a partir de um iterável (lista, tupla, etc.).
# - Retorna a nova lista ordenada.
# - A lista original não é modificada.

# Escolhi sort() porque o problema *não* pode usar função.
# Uma cópia é feita para não modificar a lista original.