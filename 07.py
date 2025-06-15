

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
# 

# sorted():
# - É uma função built-in do Python.
# - Cria uma nova lista ordenada a partir de um iterável (lista, tupla, etc.).
# - Retorna a nova lista ordenada.
# - A lista original não é modificada.

# Neste caso, utilizei o método sort() porque queria ordenar a lista
# original em ordem decrescente sem criar uma nova lista.


'''
Como o código funciona:
Inicialização:
numeros = [5, 2, 8, 1, 9, 4]: Define a lista de números.
numeros_ordenados = numeros[:]: Cria uma cópia da lista numeros usando slicing. Isso é crucial porque o método sort() modifica a lista diretamente (in-place), e a gente quer manter a lista original intacta. [:] cria uma cópia superficial da lista, o que é suficiente para o nosso caso (já que os elementos da lista são números, que são tipos imutáveis).
Ordenação:
numeros_ordenados.sort(reverse=True): Ordena a cópia da lista (numeros_ordenados) em ordem decrescente usando o método sort(). O argumento reverse=True especifica a ordem decrescente.
Impressão:
print("Lista original:", numeros) e print("Lista ordenada decrescentemente:", numeros_ordenados): Imprime a lista original (que não foi modificada) e a lista ordenada.
Explicação da diferença entre sort() e sorted():

'''